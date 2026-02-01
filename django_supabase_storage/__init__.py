"""
Django Supabase Storage

A Django storage backend for Supabase buckets.
"""

__version__ = "0.1.0"
__author__ = "Madhav Sharma"
__license__ = "MIT"

from .storage_backends import (
    SupabaseStorage,
    SupabaseMediaStorage,
    SupabaseStaticStorage,
)

__all__ = [
    "SupabaseStorage",
    "SupabaseMediaStorage",
    "SupabaseStaticStorage",
]
