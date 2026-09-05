"""
Supabase Storage Backend for Django

This backend uploads ALL files directly to Supabase buckets ONLY.
No files are ever stored locally - everything goes to Supabase.
"""

import logging
import mimetypes
from io import BytesIO
from django.contrib.staticfiles.storage import ManifestFilesMixin
from django.core.files.base import File
from django.core.files.storage import Storage
from django.conf import settings
from django.utils.dateparse import parse_datetime

try:
    from supabase import create_client
except ImportError:
    create_client = None

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class SupabaseStorage(Storage):
    """
    Supabase S3 Storage Backend

    ALL files are uploaded DIRECTLY to Supabase Storage buckets.
    NO files are stored locally - ever.

    Required Settings:
        SUPABASE_URL - Your Supabase project URL
        SUPABASE_KEY - Your Supabase public API key (anon)
        SUPABASE_BUCKET - The bucket name (e.g., 'media', 'static')
    """

    folder_path = ""

    @staticmethod
    def _normalize_name(name):
        """Normalize a path to use forward slashes (Supabase rejects backslashes as keys)."""
        return str(name).replace("\\", "/").lstrip("/") if name else ""

    def _build_storage_path(self, name):
        """Build a bucket-relative path that consistently includes folder_path."""
        cleaned_name = self._normalize_name(name)
        cleaned_folder = self._normalize_name(self.folder_path).strip("/")
        if cleaned_folder and cleaned_name:
            return f"{cleaned_folder}/{cleaned_name}"
        if cleaned_folder:
            return cleaned_folder
        return cleaned_name

    def __init__(self):
        """Initialize Supabase client."""
        # Get settings
        self.supabase_url = getattr(settings, "SUPABASE_URL", None)
        self.supabase_key = getattr(settings, "SUPABASE_KEY", None)
        self.bucket_name = getattr(settings, "SUPABASE_BUCKET", "media")

        # Validate required settings
        if not self.supabase_url:
            error_msg = (
                "SUPABASE_URL is not configured!\n"
                "Add to your .env file:\n"
                "  SUPABASE_URL=https://your-project-id.supabase.co"
            )
            logger.error(error_msg)
            raise ValueError(error_msg)

        if not self.supabase_key:
            error_msg = (
                "SUPABASE_KEY is not configured!\n"
                "Add to your .env file:\n"
                "  SUPABASE_KEY=your-anon-public-key"
            )
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Create Supabase client
        if create_client is None:
            error_msg = (
                "supabase is required but not installed!\n" "Install it with: pip install supabase"
            )
            logger.error(error_msg)
            raise ImportError(error_msg)

        try:
            self.client = create_client(self.supabase_url, self.supabase_key)
            logger.info("====== Supabase client initialized successfully ======")
        except Exception as e:
            error_msg = f"Failed to create Supabase client: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)

    def _save(self, name, content):
        """
        SAVE FILE TO SUPABASE ONLY - NEVER LOCALLY

        This is the critical method that ensures files go to Supabase.

        Args:
            name: File path/name
            content: File content (file-like object or bytes)

        Returns:
            The file path in Supabase
        """
        # Validate inputs
        if not name:
            raise ValueError("File name cannot be empty or None")

        # Clean the path
        original_name = name
        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)

        logger.info(f"====== FILE SAVE REQUEST TO SUPABASE ======")
        logger.info(
            f"Original name: {original_name}, Cleaned name: {name}, Bucket: {self.bucket_name}, Folder Path: {self.folder_path}"
        )
        # Read file content
        try:
            if hasattr(content, "read"):
                logger.debug("Content is file-like object, reading...")
                file_content = content.read()
            else:
                logger.debug("Content is bytes, using directly...")
                file_content = content

            file_size = len(file_content) if file_content is not None else 0
            logger.info(f"File size: {file_size} bytes")

            if file_content is None:
                error_msg = f"File content is None: {name}"
                logger.error(error_msg)
                raise ValueError(error_msg)

        except Exception as e:
            error_msg = f"Failed to read file content: {str(e)}"
            logger.error(error_msg)
            raise IOError(error_msg)

        # Upload to Supabase ONLY
        try:
            logger.info(f"Uploading to Supabase: {self.bucket_name}/{storage_path}")

            file_options = {"upsert": "true"}
            trust_file_extension_content_type = getattr(
                settings,
                "SUPABASE_STORAGE_TRUST_FILE_EXTENSION_CONTENT_TYPE",
                False,
            )
            default_upload_content_type = getattr(
                settings,
                "SUPABASE_STORAGE_DEFAULT_UPLOAD_CONTENT_TYPE",
                "application/octet-stream",
            )

            if trust_file_extension_content_type:
                mime_type, _ = mimetypes.guess_type(name)
                if mime_type:
                    file_options["content-type"] = mime_type
                    logger.debug(f"Detected MIME type for {name}: {mime_type}")
                else:
                    file_options["content-type"] = default_upload_content_type
                    logger.debug(
                        f"No MIME type detected for {name}; using safe default "
                        f"{default_upload_content_type}"
                    )
            else:
                file_options["content-type"] = default_upload_content_type
                logger.debug(
                    f"Using safe default content type for {name}: " f"{default_upload_content_type}"
                )

            self.client.storage.from_(self.bucket_name).upload(
                path=storage_path, file=file_content, file_options=file_options
            )

            return name

        except Exception as e:
            error_msg = (
                f"UPLOAD TO SUPABASE FAILED!\n"
                f"Error: {str(e)}\n"
                f"File: {name}\n"
                f"Bucket: {self.bucket_name}"
            )
            logger.error(error_msg)
            logger.exception("Full traceback:")
            raise IOError(error_msg)

    def _open(self, name, mode="rb"):
        """
        Open/download a file from Supabase.

        Args:
            name: File path in Supabase
            mode: File mode (ignored)

        Returns:
            BytesIO object with file content
        """
        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)
        logger.info(f"Opening file from Supabase: {self.bucket_name}/{storage_path}")

        try:
            data = self.client.storage.from_(self.bucket_name).download(storage_path)
            logger.info(f"====== File opened: {name} ======")
            return File(BytesIO(data), name=name)
        except Exception as e:
            error_msg = f"Failed to download {name}: {str(e)}"
            # Not found is an expected condition (e.g. manifest read on first collectstatic run)
            if "not_found" in str(e) or "404" in str(e):
                logger.debug(error_msg)
            else:
                logger.error(error_msg)
            raise FileNotFoundError(error_msg)

    def delete(self, name):
        """
        Delete a file from Supabase.

        Args:
            name: File path in Supabase
        """
        if not name:
            return

        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)
        logger.info(f"Deleting from Supabase: {self.bucket_name}/{storage_path}")

        try:
            self.client.storage.from_(self.bucket_name).remove([storage_path])
            logger.info(f"====== Deleted: {name} ======")
        except Exception as e:
            logger.warning(f"Could not delete {name}: {str(e)}")

    def exists(self, name):
        """
        Check if file exists in Supabase.

        Args:
            name: File path in Supabase

        Returns:
            True if exists, False otherwise
        """
        if not name:
            return False

        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)

        try:
            return self.client.storage.from_(self.bucket_name).exists(storage_path)
        except Exception:
            return False

    def listdir(self, path):
        """
        List files in a Supabase directory.

        Args:
            path: Directory path

        Returns:
            (directories, files) tuple
        """
        path = self._normalize_name(path)
        storage_path = self._build_storage_path(path)

        try:
            response = self.client.storage.from_(self.bucket_name).list(path=storage_path)
            dirs = []
            files = []

            for item in response:
                if item.get("id") is None:
                    dirs.append(item["name"])
                else:
                    files.append(item["name"])

            return dirs, files
        except Exception as e:
            logger.warning(f"Could not list directory {path}: {str(e)}")
            return [], []

    def size(self, name):
        """
        Get file size in bytes.

        Args:
            name: File path in Supabase

        Returns:
            File size or 0 if error
        """
        if not name:
            return 0

        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)

        try:
            metadata = self.client.storage.from_(self.bucket_name).info(storage_path)
            size = metadata.get("metadata", {}).get("size", 0)
            return size
        except Exception:
            return 0

    def url(self, name):
        """
        Get public URL for a file in Supabase.

        Args:
            name: File path in Supabase

        Returns:
            Public HTTPS URL to access the file
        """
        if not name:
            return ""

        name = self._normalize_name(name)

        # Construct the public URL
        storage_path = self._build_storage_path(name)
        url = f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{storage_path}"
        return url

    def get_accessed_time(self, name):
        """Get file access time."""
        return self.get_created_time(name)

    def get_created_time(self, name):
        """Get file creation time.

        Per the Storage API contract, raises NotImplementedError if unavailable
        (Django's collectstatic relies on this rather than a None return).
        """
        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)

        try:
            metadata = self.client.storage.from_(self.bucket_name).info(storage_path)
            created_at = parse_datetime(metadata.get("created_at", ""))
            if created_at is None:
                raise ValueError("created_at missing or unparsable")
            return created_at
        except Exception as e:
            raise NotImplementedError(f"Could not determine created time for {name}: {e}")

    def get_modified_time(self, name):
        """Get file modification time.

        Per the Storage API contract, raises NotImplementedError if unavailable
        (Django's collectstatic relies on this rather than a None return).
        """
        name = self._normalize_name(name)
        storage_path = self._build_storage_path(name)

        try:
            metadata = self.client.storage.from_(self.bucket_name).info(storage_path)
            updated_at = parse_datetime(metadata.get("updated_at", ""))
            if updated_at is None:
                raise ValueError("updated_at missing or unparsable")
            return updated_at
        except Exception as e:
            raise NotImplementedError(f"Could not determine modified time for {name}: {e}")


class SupabaseMediaStorage(SupabaseStorage):
    """
    Media Files Storage (e.g., uploads, images, documents)

    All user uploads go to the 'media' bucket in Supabase.
    """

    folder_path = "media"

    def __init__(self):
        super().__init__()
        self.bucket_name = getattr(
            settings,
            "SUPABASE_MEDIA_BUCKET",
            getattr(settings, "SUPABASE_BUCKET", self.bucket_name or "media"),
        )
        logger.info(f"====== SupabaseMediaStorage initialized for Media bucket ======")


class SupabaseStaticStorageBase(SupabaseStorage):
    """
    Static Files Storage (CSS, JavaScript, Images, etc.)

    All static files go to the 'static' bucket in Supabase.
    """

    folder_path = "static"

    def __init__(self):
        super().__init__()
        self.bucket_name = getattr(
            settings,
            "SUPABASE_STATIC_BUCKET",
            getattr(settings, "SUPABASE_BUCKET", self.bucket_name or "static"),
        )
        logger.info("====== SupabaseStaticStorage initialized for Static bucket ======")


class SupabaseStaticStorageNoManifest(SupabaseStaticStorageBase):
    """Static storage without manifest hashing."""


class SupabaseStaticStorage(ManifestFilesMixin, SupabaseStaticStorageBase):
    """
    Static storage with manifest hashing enabled by default.

    Set SUPABASE_STATIC_MANIFEST = False to opt out and use plain static names.
    """

    def __new__(cls, *args, **kwargs):
        use_manifest = getattr(settings, "SUPABASE_STATIC_MANIFEST", True)
        if cls is SupabaseStaticStorage and not use_manifest:
            return SupabaseStaticStorageNoManifest(*args, **kwargs)
        return super().__new__(cls)
