from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'PurGPT.py, the wrapper for the PurGPT API'
with open("README.md", "r") as fh:
  LONG_DESCRIPTION = fh.read()

# Setting up
setup(
        name="PurGPT.py", 
        version=VERSION,
        author="TheCatsMoo",
        author_email="tcm@tcm.gay",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=["requests"], 

        keywords=['purgpt', 'AI'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)