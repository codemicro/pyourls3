import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyourls3",
    version="1.0.0",
    author="Thomas Pain",
    author_email="pyourls3@tdpain.net",
    description="A Python 3 API wrapper for YOURLS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codemicro/pyourls3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public Licence 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)