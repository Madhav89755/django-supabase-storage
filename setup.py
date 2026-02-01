"""Setup configuration for django-supabase-storage package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-supabase-storage",
    version="0.1.1",
    author="Madhav Sharma",
    author_email="madhav.sharma2002.12@gmail.com",
    license="MIT",
    description="Django storage backend for Supabase buckets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madhav89755/django-supabase-storage",
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",
        "supabase>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-django",
            "black",
            "flake8",
            "isort",
        ],
    },
    include_package_data=True,
    keywords="django storage supabase",
    project_urls={
        "Bug Reports": "https://github.com/madhav89755/django-supabase-storage/issues",
        "Source": "https://github.com/madhav89755/django-supabase-storage",
    },
)
