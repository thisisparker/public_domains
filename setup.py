import sys
import setuptools

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    dependencies = f.read().split()

if __name__ == "__main__":
    setuptools.setup(
        name="public_domains",
        version="0.0.6",
        url="https://github.com/edsu/public_domains",
        author="Ed Summers",
        author_email="ehs@pobox.com",
        py_modules=["public_domains"],
        description="Find possible host names in a source text",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        classifiers=[
            "License :: OSI Approved :: MIT License",
        ],
        python_requires=">=2.7",
        install_requires=dependencies,
        setup_requires=["pytest-runner"],
        tests_require=[
            "pytest",
        ],
        entry_points={
            "console_scripts": [
                "public_domains = public_domains:main"
            ]
        },
    )
