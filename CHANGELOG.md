# Changelog

All notable changes to django-supabase-storage will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned

- Advanced caching support for frequently accessed files
- Signed URL generation for temporary access
- Support for multipart uploads for large files
- Batch operations for bulk file management
- Custom metadata support for files
- S3-compatible API support

---

## [0.1.1] - 2026-02-02

### 🎉 Initial Release

This is the first stable release of django-supabase-storage!

### Added

#### Core Features

- **SupabaseStorage**: Base storage backend for Supabase buckets
- **SupabaseMediaStorage**: Pre-configured storage for media files
- **SupabaseStaticStorage**: Pre-configured storage for static files
- Complete Django Storage API implementation with all required methods:
   - `save()` - Save files to Supabase buckets
   - `open()` - Open and read files from buckets
   - `delete()` - Delete files from buckets
   - `exists()` - Check if file exists
   - `listdir()` - List directory contents
   - `size()` - Get file size
   - `url()` - Generate public URLs
   - `get_accessed_time()` - Get last access time
   - `get_created_time()` - Get creation time
   - `get_modified_time()` - Get modification time

#### Configuration

- Support for Django 3.2, 4.0, 4.1, 4.2, and 5.0
- Support for both old (`DEFAULT_FILE_STORAGE`) and new (`STORAGES`) configuration
- Environment variable support for `SUPABASE_URL` and `SUPABASE_KEY`
- Configurable folder paths for organizing files
- Automatic bucket creation and management

#### Error Handling & Logging

- Comprehensive error handling for all operations
- Detailed logging for debugging and monitoring
- Clear error messages for common issues
- Graceful fallback for missing dependencies

#### Documentation

- Complete README with usage examples
- Quick Start guide (5-minute setup)
- Production deployment guide (Docker, Vercel, Lambda, Railway, DigitalOcean)
- Troubleshooting guide with 20+ solutions
- FAQ with 100+ answered questions
- API reference documentation
- Contributing guidelines
- Installation guide
- Multiple learning paths for different user levels

#### Package Infrastructure

- Proper Python package structure
- PyPI publishing support
- Modern `pyproject.toml` configuration
- Traditional `setup.py` for compatibility
- Development dependencies specified
- MIT License

### Security

- Secure credential handling via environment variables
- No hardcoded credentials in code
- Support for Supabase Row Level Security (RLS) policies
- HTTPS enforcement recommendations
- Security best practices documentation

### Performance

- Efficient file operations with Supabase SDK
- Minimal overhead for storage operations
- Optimized URL generation
- Support for CDN caching via Supabase

### Developer Experience

- Clear and comprehensive documentation 
- Multiple installation methods
- Verification tools for quick debugging
- Helpful error messages
- Type hints and docstrings

### Compatibility

- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Django**: 3.2, 4.0, 4.1, 4.2, 5.0
- **Supabase SDK**: 2.0.0+

### Known Issues

- None reported

### Contributors

- Madhav Sharma (@Madhav89755) - Initial implementation and documentation

---

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backward-compatible manner
- **PATCH** version for backward-compatible bug fixes

### Release Types

#### Major Releases (X.0.0)

- Breaking changes to the API
- Removal of deprecated features
- Major architectural changes
- Significant new features that change core behavior

#### Minor Releases (0.X.0)

- New features that are backward-compatible
- Deprecation warnings for features to be removed
- Performance improvements
- New documentation sections

#### Patch Releases (0.0.X)

- Bug fixes
- Documentation improvements
- Performance optimizations without API changes
- Security patches

---

## Deprecation Notices

### Current

- No deprecations in this release

### Planned Deprecations

- None currently planned

---

## Security Advisories

### Current

- No security advisories

### Reporting Security Issues

Please report security vulnerabilities to: madhav.sharma2002.12@gmail.com

Do not open public GitHub issues for security vulnerabilities.

---

## Acknowledgments

### Inspiration

- Django's file storage system
- Supabase's excellent storage API
- The Django and Supabase communities

### Dependencies

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Supabase Python SDK](https://github.com/supabase-community/supabase-py) - Python client for Supabase

---

## Links

- **Homepage**: https://github.com/Madhav89755/django-supabase-storage
- **PyPI**: https://pypi.org/project/django-supabase-storage/
- **Issues**: https://github.com/Madhav89755/django-supabase-storage/issues
- **Discussions**: https://github.com/Madhav89755/django-supabase-storage/discussions

---

## Stay Updated

- ⭐ Star the project on GitHub
- 👁️ Watch for updates
- 🐛 Report issues
- 💡 Suggest features
- 🤝 Contribute code

---

_For detailed installation instructions, see [INSTALLATION.md](INSTALLATION.md)_  
_For usage examples, see [QUICK_START.md](QUICK_START.md)_  
_For complete documentation, see [README.md](README.md)_

---

**Last Updated**: February 2, 2026  
**Current Version**: 0.1.1
**Status**: Stable  
**License**: MIT
