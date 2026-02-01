#!/usr/bin/env python
"""
Test script to verify the django-supabase-storage package can be imported and configured.
"""

import sys
import os

# Add the package directory to the path for testing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("Testing django-supabase-storage Package Import")
print("=" * 70)

# Test 1: Import the package
print("\n1. Testing package import...")
try:
    import django_supabase_storage
    print("   ✓ Successfully imported django_supabase_storage")
    print(f"   Version: {django_supabase_storage.__version__}")
except Exception as e:
    print(f"   ✗ Failed to import django_supabase_storage: {e}")
    sys.exit(1)

# Test 2: Check if classes are available
print("\n2. Checking if storage classes are available...")
try:
    from django_supabase_storage import (
        SupabaseStorage,
        SupabaseMediaStorage,
        SupabaseStaticStorage,
    )
    print("   ✓ SupabaseStorage")
    print("   ✓ SupabaseMediaStorage")
    print("   ✓ SupabaseStaticStorage")
except Exception as e:
    print(f"   ✗ Failed to import storage classes: {e}")
    sys.exit(1)

# Test 3: Try importing as backend string (simulating Django settings)
print("\n3. Testing Django backend string imports...")
backend_strings = [
    'django_supabase_storage.SupabaseMediaStorage',
    'django_supabase_storage.SupabaseStaticStorage',
    'django_supabase_storage.SupabaseStorage',
]

for backend_str in backend_strings:
    try:
        module_path, class_name = backend_str.rsplit('.', 1)
        module = __import__(module_path, fromlist=[class_name])
        cls = getattr(module, class_name)
        print(f"   ✓ {backend_str}")
    except Exception as e:
        print(f"   ✗ {backend_str}: {e}")
        sys.exit(1)

print("\n" + "=" * 70)
print("All Import Tests Passed!")
print("=" * 70)

print("\n📝 Configuration Example:")
print("""
# In your Django settings.py:

import os

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# For Django 4.2+
STORAGES = {
    'default': {
        'BACKEND': 'django_supabase_storage.SupabaseMediaStorage',
    },
    'staticfiles': {
        'BACKEND': 'django_supabase_storage.SupabaseStaticStorage',
    },
}

# For Django < 4.2
# DEFAULT_FILE_STORAGE = 'django_supabase_storage.SupabaseMediaStorage'
# STATICFILES_STORAGE = 'django_supabase_storage.SupabaseStaticStorage'
""")
