from setuptools import setup, find_packages

# Read the README content for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="codebasedutils",
    version="0.0.1",
    packages=find_packages(),
    author="Alex Figueroa",
    author_email="alexfigueroa.solutions@gmail.com",
    description="CodebasedUtils is a versatile CLI tool designed to supercharge your developer workflow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cybrvybe/CodebasedUtils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'util=core.main:util',
        ],
    }
)
