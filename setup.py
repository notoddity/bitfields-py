from setuptools import setup

readme = ''
with open("README.md") as f:
    readme = f.read()

setup(
    name="altflags",
    author="Oddity",
    version="0.0.3",
    license="MIT",
    description="Python alternative (binary) flags",
    python_requires=">=3.8.0",
    packages=["altflags"],
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)