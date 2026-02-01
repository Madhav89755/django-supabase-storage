#!/usr/bin/env python
"""
Setup Verification Script for django-supabase-storage

This script verifies that your django-supabase-storage installation is correct
and that all dependencies are properly configured.

Usage:
    python verify_setup.py
"""

import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def print_success(text):
    """Print success message"""
    print(f"✓ {text}")

def print_error(text):
    """Print error message"""
    print(f"✗ {text}")

def print_warning(text):
    """Print warning message"""
    print(f"⚠ {text}")

def print_info(text):
    """Print info message"""
    print(f"ℹ {text}")

def check_python_version():
    """Check Python version"""
    print_header("1. Python Version Check")
    
    version = sys.version_info
    version_string = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 8:
        print_success(f"Python {version_string} (required: 3.8+)")
        return True
    else:
        print_error(f"Python {version_string} (required: 3.8+)")
        return False

def check_django():
    """Check Django installation and version"""
    print_header("2. Django Installation Check")
    
    try:
        import django
        version = django.__version__
        
        major, minor = int(version.split('.')[0]), int(version.split('.')[1])
        
        if major >= 3 and minor >= 2:
            print_success(f"Django {version} installed (required: 3.2+)")
            return True
        else:
            print_error(f"Django {version} (required: 3.2+)")
            return False
    except ImportError:
        print_error("Django is not installed")
        print_info("Install with: pip install django")
        return False

def check_supabase():
    """Check Supabase SDK installation"""
    print_header("3. Supabase SDK Check")
    
    try:
        import supabase
        version = supabase.__version__ if hasattr(supabase, '__version__') else "unknown"
        print_success(f"Supabase SDK installed (version: {version})")
        return True
    except ImportError:
        print_error("Supabase SDK is not installed")
        print_info("Install with: pip install supabase>=2.0.0")
        return False

def check_django_supabase_storage():
    """Check django-supabase-storage installation"""
    print_header("4. django-supabase-storage Package Check")
    
    try:
        import django_supabase_storage
        version = django_supabase_storage.__version__
        print_success(f"django-supabase-storage {version} installed")
        
        # Check for required classes
        from django_supabase_storage import (
            SupabaseStorage,
            SupabaseMediaStorage,
            SupabaseStaticStorage,
        )
        
        print_success("SupabaseStorage class available")
        print_success("SupabaseMediaStorage class available")
        print_success("SupabaseStaticStorage class available")
        
        return True
    except ImportError as e:
        print_error(f"django-supabase-storage is not installed: {e}")
        print_info("Install with: pip install django-supabase-storage")
        return False

def check_environment_variables():
    """Check environment variables"""
    print_header("5. Environment Variables Check")
    
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    
    all_set = True
    
    if supabase_url:
        print_success(f"SUPABASE_URL is set: {supabase_url[:50]}...")
    else:
        print_warning("SUPABASE_URL is not set")
        all_set = False
    
    if supabase_key:
        print_success(f"SUPABASE_KEY is set: {supabase_key[:20]}...")
    else:
        print_warning("SUPABASE_KEY is not set")
        all_set = False
    
    if not all_set:
        print_info("Set environment variables:")
        print_info("  export SUPABASE_URL=https://your-project-id.supabase.co")
        print_info("  export SUPABASE_KEY=your-anon-public-key")
    
    return all_set

def check_dotenv():
    """Check if python-dotenv is installed"""
    print_header("6. Optional Dependencies Check")
    
    try:
        import dotenv
        print_success("python-dotenv is installed (optional but recommended)")
    except ImportError:
        print_warning("python-dotenv is not installed (optional)")
        print_info("Install with: pip install python-dotenv")

def check_django_settings():
    """Check if Django settings are configured"""
    print_header("7. Django Settings Configuration Check")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
        import django
        django.setup()
        
        from django.conf import settings
        
        # Check for Supabase settings
        if hasattr(settings, 'SUPABASE_URL'):
            print_success(f"SUPABASE_URL configured: {settings.SUPABASE_URL[:50]}...")
        else:
            print_warning("SUPABASE_URL not configured in Django settings")
        
        if hasattr(settings, 'SUPABASE_KEY'):
            print_success(f"SUPABASE_KEY configured: {settings.SUPABASE_KEY[:20]}...")
        else:
            print_warning("SUPABASE_KEY not configured in Django settings")
        
        # Check for storage settings
        if hasattr(settings, 'STORAGES'):
            print_success("STORAGES configuration found (Django 4.2+)")
            if 'default' in settings.STORAGES:
                backend = settings.STORAGES['default'].get('BACKEND', 'Not set')
                print_success(f"  Default storage: {backend}")
            if 'staticfiles' in settings.STORAGES:
                backend = settings.STORAGES['staticfiles'].get('BACKEND', 'Not set')
                print_success(f"  Static storage: {backend}")
        elif hasattr(settings, 'DEFAULT_FILE_STORAGE'):
            print_success(f"DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
            if hasattr(settings, 'STATICFILES_STORAGE'):
                print_success(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
        else:
            print_warning("No storage configuration found")
        
        return True
    except Exception as e:
        print_warning(f"Could not verify Django settings: {e}")
        print_info("Make sure DJANGO_SETTINGS_MODULE is set correctly")
        return False

def test_storage_import():
    """Test if storage backends can be imported directly"""
    print_header("8. Storage Backend Import Test")
    
    try:
        from django_supabase_storage import SupabaseMediaStorage, SupabaseStaticStorage
        print_success("SupabaseMediaStorage can be imported")
        print_success("SupabaseStaticStorage can be imported")
        return True
    except Exception as e:
        print_error(f"Failed to import storage backends: {e}")
        return False

def generate_config_example():
    """Generate a configuration example"""
    print_header("9. Configuration Example")
    
    print("Add the following to your Django settings.py:\n")
    print("""
import os
from dotenv import load_dotenv

load_dotenv()

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Storage Configuration (Django 4.2+)
STORAGES = {
    'default': {
        'BACKEND': 'django_supabase_storage.SupabaseMediaStorage',
    },
    'staticfiles': {
        'BACKEND': 'django_supabase_storage.SupabaseStaticStorage',
    },
}

# For Django < 4.2, use:
# DEFAULT_FILE_STORAGE = 'django_supabase_storage.SupabaseMediaStorage'
# STATICFILES_STORAGE = 'django_supabase_storage.SupabaseStaticStorage'
""")
    
    print("\nCreate a .env file in your project root:\n")
    print("""
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-public-key
""")

def main():
    """Run all checks"""
    print_header("django-supabase-storage Setup Verification")
    
    checks = [
        ("Python Version", check_python_version),
        ("Django Installation", check_django),
        ("Supabase SDK", check_supabase),
        ("Package Installation", check_django_supabase_storage),
        ("Environment Variables", check_environment_variables),
        ("Storage Import", test_storage_import),
    ]
    
    results = {}
    
    for name, check_func in checks:
        try:
            results[name] = check_func()
        except Exception as e:
            print_error(f"Error checking {name}: {e}")
            results[name] = False
    
    check_dotenv()
    
    # Optional Django checks
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
        import django
        django.setup()
        check_django_settings()
    except Exception as e:
        print_warning(f"Could not check Django settings: {e}")
    
    generate_config_example()
    
    # Print summary
    print_header("Verification Summary")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for name, passed_check in results.items():
        status = "✓ PASS" if passed_check else "✗ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n{passed}/{total} checks passed\n")
    
    if passed == total:
        print_success("All critical checks passed! Your setup is ready.")
        print_info("Next steps:")
        print_info("1. Create Supabase buckets (media and static)")
        print_info("2. Configure storage bucket policies for public read access")
        print_info("3. Test with: python manage.py shell")
        print_info("4. See QUICK_START.md for detailed usage examples")
        return 0
    else:
        print_error(f"Some checks failed. Please fix the issues above.")
        print_info("See TROUBLESHOOTING.md for help with common issues")
        return 1

if __name__ == '__main__':
    sys.exit(main())
