# Installation Guide

Complete installation guide for django-supabase-storage.

## Table of Contents

1. [Quick Installation](#quick-installation)
2. [Installation Methods](#installation-methods)
3. [Prerequisites](#prerequisites)
4. [Development Installation](#development-installation)
5. [Verification](#verification)
6. [Next Steps](#next-steps)
7. [Troubleshooting](#troubleshooting)

---

## Quick Installation

### Using pip (Recommended)

```bash
pip install django-supabase-storage

```

That's it! Skip to [Verification](#verification) to confirm installation.

---

## Installation Methods

### Method 1: Install from PyPI

**Best for**: Production use, stable releases

```bash
pip install django-supabase-storage

```

Install specific version:

```bash
pip install django-supabase-storage==1.0.0

```

Upgrade to latest version:

```bash
pip install --upgrade django-supabase-storage

```

---

### Method 2: Install from GitHub

**Best for**: Latest features, testing unreleased versions

```bash
pip install git+https://github.com/Madhav89755/django-supabase-storage.git

```

Install specific branch:

```bash
pip install git+https://github.com/Madhav89755/django-supabase-storage.git@main

```

Install specific commit or tag:

```bash
pip install git+https://github.com/Madhav89755/django-supabase-storage.git@v1.0.0

```

---

### Method 3: Install from Source

**Best for**: Development, contributing, customization

#### Step 1: Clone Repository

```bash
git clone https://github.com/Madhav89755/django-supabase-storage.git
cd django-supabase-storage

```

#### Step 2: Install in Development Mode

```bash
pip install -e .

```

Or with development dependencies:

```bash
pip install -e ".[dev]"

```

---

### Method 4: Using requirements.txt

**Best for**: Project dependency management

Add to your `requirements.txt`:

```txt
django-supabase-storage==1.0.0

```

Or for latest version:

```txt
django-supabase-storage

```

Then install:

```bash
pip install -r requirements.txt

```

---

### Method 5: Using Poetry

**Best for**: Modern Python projects using Poetry

```bash
poetry add django-supabase-storage

```

Or add to `pyproject.toml`:

```toml
[tool.poetry.dependencies]
django-supabase-storage = "^1.0.0"

```

Then run:

```bash
poetry install

```

---

### Method 6: Using Pipenv

**Best for**: Projects using Pipenv

```bash
pipenv install django-supabase-storage

```

---

## Prerequisites

### Required

- **Python**: 3.8 or higher
- **Django**: 3.2 or higher
- **Supabase Python SDK**: 2.0.0 or higher

### Check Your Versions

```bash
# Check Python version
python --version

# Check Django version
python -c "import django; print(django.__version__)"

# Check if Supabase is installed
python -c "import supabase; print('Supabase SDK installed')"

```

### Install Dependencies

If you don't have Django or Supabase SDK:

```bash
# Install Django
pip install Django>=3.2

# Install Supabase SDK
pip install supabase>=2.0.0

# Or install both at once
pip install Django>=3.2 supabase>=2.0.0

```

---

## Development Installation

For contributing or customizing the package:

### 1. Fork and Clone

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/django-supabase-storage.git
cd django-supabase-storage

```

### 2. Create Virtual Environment

#### Using venv

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

#### Using virtualenv

```bash
virtualenv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

#### Using conda

```bash
conda create -n django-supabase python=3.11
conda activate django-supabase

```

### 3. Install Development Dependencies

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

```

This installs:

- Main package dependencies (Django, Supabase)
- Development tools (pytest, black, flake8, isort)

### 4. Verify Installation

```bash
# Run tests (if available)
pytest

# Check code style
black --check .
flake8 .
isort --check .

```

---

## Verification

After installation, verify everything works:

### Step 1: Check Package Import

```bash
python -c "import django_supabase_storage; print('✓ Package installed successfully')"

```

### Step 2: Check Version

```bash
python -c "import django_supabase_storage; print(f'Version: {django_supabase_storage.__version__}')"

```

### Step 3: Check Classes Available

```bash
python -c "from django_supabase_storage import SupabaseStorage, SupabaseMediaStorage, SupabaseStaticStorage; print('✓ All classes available')"

```

### Step 4: Run Verification Script

If you have the repository files:

```bash
python verify_setup.py

```

This comprehensive script checks:

- Python version
- Django installation
- Supabase SDK
- Package installation
- Environment variables
- Import functionality

---

## Next Steps

After successful installation:

### 1. Set Up Supabase

1. Create a [Supabase account](https://app.supabase.com)
2. Create a new project
3. Get your credentials:
   - Project URL (Settings → API)
   - Anon public key (Settings → API)

### 2. Configure Django Settings

Add to your `settings.py`:

```python
import os

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET_NAME")

# Storage Configuration (Django 4.2+)
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

```

### 3. Set Environment Variables

Create `.env` file:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-public-key
SUPABASE_BUCKET_NAME=your-supabase-bucket-name
```

Load in Django:

```python
# settings.py
from dotenv import load_dotenv
load_dotenv()

```

### 4. Create Supabase Buckets

In Supabase Dashboard:

1. Go to Storage
2. Create bucket: `media`
3. Create bucket: `static`
4. Set public access policies

### 5. Test Installation

```bash
python manage.py shell

```

```python
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Test upload
content = ContentFile(b"Test content")
path = default_storage.save('test.txt', content)
print(f"✓ File saved: {path}")

# Test URL
url = default_storage.url(path)
print(f"✓ URL: {url}")

# Clean up
default_storage.delete(path)
print("✓ File deleted")

```

### 6. Read Documentation

- __[QUICK_START.md](QUICK_START.md)__ - 5-minute setup guide
- **[README.md](README.md)** - Complete documentation
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment
- **[FAQ.md](FAQ.md)** - Common questions

---

## Troubleshooting

### Issue: "No module named 'django_supabase_storage'"

**Solution**:

```bash
# Verify pip installation
pip show django-supabase-storage

# Reinstall
pip install --force-reinstall --no-cache-dir django-supabase-storage

# Check Python path
python -c "import sys; print(sys.path)"

```

---

### Issue: "Could not find a version that satisfies the requirement"

**Solution**:

```bash
# Update pip
pip install --upgrade pip

# Try again
pip install django-supabase-storage

```

---

### Issue: "ImportError: cannot import name 'SupabaseStorage'"

**Possible causes**:

1. Supabase SDK not installed
2. Incorrect package version

**Solution**:

```bash
# Install Supabase SDK
pip install supabase>=2.0.0

# Reinstall package
pip install --upgrade --force-reinstall django-supabase-storage

```

---

### Issue: Version conflicts with Django

**Solution**:

```bash
# Check Django version
python -c "import django; print(django.__version__)"

# Install compatible version
pip install "Django>=3.2,<6.0"

```

---

### Issue: SSL Certificate Error

**Solution**:

```bash
# Upgrade certifi
pip install --upgrade certifi

# Or install with trusted host (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org django-supabase-storage

```

---

### Issue: Permission Denied (Windows)

**Solution**:

```bash
# Run as administrator or use --user flag
pip install --user django-supabase-storage

```

---

### Issue: Installation in Virtual Environment

**Solution**:

```bash
# Make sure virtual environment is activated
# You should see (.venv) or (venv) in your prompt

# Activate venv (Linux/Mac)
source .venv/bin/activate

# Activate venv (Windows)
.venv\Scripts\activate

# Then install
pip install django-supabase-storage

```

---

## Platform-Specific Installation

### Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

```

In `requirements.txt`:

```txt
Django>=3.2
supabase>=2.0.0
django-supabase-storage

```

Build and run:

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp

```

---

### Heroku

Add to `requirements.txt`:

```txt
django-supabase-storage

```

Heroku automatically installs on deploy.

---

### AWS Lambda / Serverless

Use layer or package dependencies:

```bash
pip install django-supabase-storage -t package/
cd package
zip -r ../deployment.zip .

```

---

### Google Cloud Run

In `requirements.txt`:

```txt
django-supabase-storage

```

Cloud Run installs automatically from `requirements.txt`.

---

## Upgrading

### From pip

```bash
pip install --upgrade django-supabase-storage

```

### Check what will be upgraded

```bash
pip install --upgrade --dry-run django-supabase-storage

```

### Upgrade to specific version

```bash
pip install --upgrade django-supabase-storage==0.2.0

```

---

## Uninstallation

```bash
pip uninstall django-supabase-storage

```

Confirm when prompted, or use `-y` for automatic yes:

```bash
pip uninstall -y django-supabase-storage

```

---

## Getting Help

### Documentation

- [Quick Start Guide](QUICK_START.md)
- [Complete Documentation](README.md)
- [Troubleshooting Guide](TROUBLESHOOTING.md)
- [FAQ](FAQ.md)

### Tools

- Run `python verify_setup.py` for comprehensive checks
- Use `example_settings.py` for configuration template

### Support

- [GitHub Issues](https://github.com/Madhav89755/django-supabase-storage/issues)
- [GitHub Discussions](https://github.com/Madhav89755/django-supabase-storage/discussions)

---

## Summary

**Quick Installation**:

```bash
pip install django-supabase-storage

```

**Verification**:

```bash
python -c "import django_supabase_storage; print('✓ Success')"

```

__Next Step__:
Read [QUICK_START.md](QUICK_START.md) for setup instructions.

---

*Last Updated: February 2026*  
*Package Version: 1.0.0+*  
*Maintained: Yes*