import setuptools

# Creates
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyresume-mwklose",
    version="0.0.1",
    author="Mark Klose",
    author_email="mklose@unc.edu",
    description="Automatically generates resumes and CVs using CSVs and Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwklose/pyresume",
    project_urls={
        "Bug Tracker": "https://github.com/mwklose/pyresume/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)