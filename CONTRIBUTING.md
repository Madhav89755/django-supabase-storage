# Contributing to django-supabase-storage

Thank you for your interest in contributing to django-supabase-storage! We welcome contributions from everyone.

## Table of Contents

1. Getting Started
2. Development Setup
3. How to Contribute
4. Code Guidelines
5. Testing
6. Documentation
7. Pull Request Process
8. Community Guidelines

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Supabase account (for testing)
- Git
- GitHub account

### First Time Contributors

If this is your first time contributing to an open-source project:

1. Read this guide completely
2. Look for issues labeled "good first issue" or "help wanted"
3. Ask questions in GitHub Discussions if you're unsure
4. Don't be afraid to make mistakes - we're here to help!

---

## Development Setup

### 1. Fork the Repository

1. Visit https://github.com/Madhav89755/django-supabase-storage
2. Click the "Fork" button in the top right
3. This creates a copy of the repository in your GitHub account

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/django-supabase-storage.git
cd django-supabase-storage

```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/Madhav89755/django-supabase-storage.git
git fetch upstream

```

### 4. Create Virtual Environment

```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Using conda
conda create -n django-supabase python=3.11
conda activate django-supabase

```

### 5. Install Development Dependencies

```bash
pip install -e ".[dev]"

```

This installs:

- Main dependencies (Django, Supabase)
- Development tools (pytest, black, flake8, isort)

### 6. Set Up Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=https://your-test-project.supabase.co
SUPABASE_KEY=your-test-anon-key
SUPABASE_BUCKET_NAME=your-supabase-bucket-name
```

---

## How to Contribute

### Types of Contributions

We welcome:

1. **Bug Fixes** - Fix issues reported on GitHub
2. **New Features** - Add new functionality (discuss first!)
3. **Documentation** - Improve or add documentation
4. **Tests** - Add or improve test coverage
5. **Examples** - Provide usage examples
6. **Code Quality** - Refactoring, optimization

### Finding Issues to Work On

1. Browse [GitHub Issues](https://github.com/Madhav89755/django-supabase-storage/issues)
2. Look for labels:
   - `good first issue` - Great for beginners
   - `help wanted` - We need help with this
   - `bug` - Something isn't working
   - `enhancement` - New feature request
   - `documentation` - Documentation improvements

### Before Starting Work

1. **Check if someone else is working on it**

   - Look at issue comments
   - Check open pull requests

2. **Comment on the issue**

   - Let others know you're working on it
   - Ask questions if needed

3. **For major changes**

   - Open an issue first to discuss
   - Get feedback before implementing

---

## Code Guidelines

### Python Style

We follow [PEP 8](https://pep8.org/) with some modifications:

- Maximum line length: 88 characters (Black default)
- Use double quotes for strings
- Use trailing commas in multi-line structures

### Code Formatting

We use **Black** for automatic formatting:

```bash
# Format all files
black .

# Check formatting without changes
black --check .

```

### Linting

We use **flake8** for linting:

```bash
# Run linter
flake8 .

# Configuration is in setup.cfg

```

### Import Sorting

We use **isort** for organizing imports:

```bash
# Sort imports
isort .

# Check import order
isort --check .

```

### Type Hints

Use type hints where possible:

```python
from typing import Optional, Dict, Any

def save_file(name: str, content: bytes) -> str:
    """Save a file to Supabase storage."""
    pass

```

### Docstrings

Use Google-style docstrings:

```python
def save_file(name: str, content: bytes) -> str:
    """Save a file to Supabase storage.
    
    Args:
        name: The name/path for the file
        content: The file content as bytes
        
    Returns:
        The path where the file was saved
        
    Raises:
        ValueError: If name is empty
        IOError: If upload fails
    """
    pass

```

### Logging

Use Python's logging module:

```python
import logging

logger = logging.getLogger(__name__)

# Use appropriate levels
logger.debug("Detailed information")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred")

```

---

## Testing

### Writing Tests

1. Place tests in `tests/` directory
2. Name test files `test_*.py`
3. Name test functions `test_*`
4. Use pytest fixtures for setup

Example test:

```python
import pytest
from django_supabase_storage import SupabaseMediaStorage

def test_storage_initialization():
    """Test that storage can be initialized."""
    storage = SupabaseMediaStorage()
    assert storage is not None
    
def test_save_file():
    """Test file saving."""
    storage = SupabaseMediaStorage()
    content = ContentFile(b"test content")
    path = storage.save('test.txt', content)
    assert path == 'media/test.txt'

```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_storage.py

# Run with coverage
pytest --cov=django_supabase_storage

# Run with verbose output
pytest -v

```

### Test Coverage

We aim for >80% test coverage. Check coverage:

```bash
pytest --cov=django_supabase_storage --cov-report=html
# Open htmlcov/index.html in browser

```

---

## Documentation

### What to Document

1. **Code Comments** - Explain complex logic
2. **Docstrings** - Document all public functions/classes
3. **README Updates** - For new features
4. **API Reference** - Document all public APIs
5. **Examples** - Add usage examples

### Documentation Files

- `README.md` - Main documentation
- `QUICK_START.md` - Quick setup guide
- `DEPLOYMENT.md` - Deployment instructions
- `TROUBLESHOOTING.md` - Common issues
- `FAQ.md` - Frequently asked questions
- `CONTRIBUTING.txt` - This file
- `CHANGELOG.md` - Version history

### Writing Good Documentation

1. **Be Clear** - Use simple, direct language
2. **Be Concise** - Get to the point quickly
3. **Use Examples** - Show, don't just tell
4. **Keep Updated** - Update docs with code changes
5. **Test Examples** - Make sure code examples work

---

## Pull Request Process

### 1. Create a Branch

```bash
# Update main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description

```

### 2. Make Your Changes

```bash
# Make changes to code
# ...

# Format code
black .
isort .

# Check linting
flake8 .

# Run tests
pytest

```

### 3. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "Add feature: brief description

Detailed explanation of what changed and why.

Fixes #123"

```

Commit message format:

- First line: Brief summary (50 chars or less)
- Blank line
- Detailed explanation if needed
- Reference issue numbers with "Fixes #123"

### 4. Push to Your Fork

```bash
git push origin feature/your-feature-name

```

### 5. Open Pull Request

1. Go to GitHub repository
2. Click "Pull Request" button
3. Select your branch
4. Fill in PR template:
   - Description of changes
   - Related issue numbers
   - Testing performed
   - Screenshots (if UI changes)

### 6. Code Review Process

1. **Automated Checks**

   - Code formatting (Black)
   - Linting (flake8)
   - Tests (pytest)
   - All must pass

2. **Human Review**

   - Maintainers will review code
   - May request changes
   - Discussion in PR comments

3. **Make Updates**

```bash
# Make requested changes
# ...

# Commit and push
git add .
git commit -m "Address review comments"
git push origin feature/your-feature-name

```

4. **Merge**

   - Once approved, maintainers will merge
   - Your changes will be in the next release!

---

## Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment:

1. **Be Respectful** - Treat everyone with respect
2. **Be Constructive** - Provide helpful feedback
3. **Be Patient** - Everyone is learning
4. **Be Inclusive** - Welcome diverse perspectives
5. **Be Professional** - Keep discussions on topic

### Communication Channels

- **GitHub Issues** - Bug reports, feature requests
- **GitHub Discussions** - General questions, ideas
- **Pull Requests** - Code contributions
- **Email** - madhav.sharma2002.12@gmail.com (maintainer)

### Getting Help

If you're stuck:

1. Check existing documentation
2. Search closed issues
3. Ask in GitHub Discussions
4. Comment on related issues
5. Reach out to maintainers

---

## Development Tips

### Keeping Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Update main branch
git checkout main
git merge upstream/main
git push origin main

# Update feature branch
git checkout feature/your-feature-name
git rebase main

```

### Testing Locally

```bash
# Install package in editable mode
pip install -e .

# Test in a Django project
cd /path/to/test/django/project
python manage.py shell

>>> from django_supabase_storage import SupabaseMediaStorage
>>> storage = SupabaseMediaStorage()
>>> # Test your changes

```

### Debugging

```bash
# Run with verbose logging
export DEBUG=true
python manage.py shell

# Use pdb for debugging
import pdb; pdb.set_trace()

```

---

## Release Process

(For maintainers)

1. Update CHANGELOG.md
2. Bump version in setup.py and __init__.py
3. Create git tag
4. Build distribution
5. Upload to PyPI
6. Create GitHub release

---

## Questions?

- Open an issue for bugs or features
- Use GitHub Discussions for questions
- Email maintainers for security issues
- Check FAQ.md for common questions

---

## Thank You!

Your contributions make django-supabase-storage better for everyone. We appreciate your time and effort!

---

**Project**: django-supabase-storage
**Maintainer**: Madhav Sharma (@Madhav89755)
**License**: MIT
**Last Updated**: February 2, 2026
