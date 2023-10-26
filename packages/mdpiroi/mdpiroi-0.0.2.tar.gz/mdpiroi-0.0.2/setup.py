import pathlib
from setuptools import setup

# The directory containing this file
dir = pathlib.Path(__file__).parent

# README file
README = (dir / "README.md").read_text()

setup(
    name='mdpiroi',
    version="0.0.02",
    description=("library for ML"),
    long_description=README,
    long_description_content_type="text/markdown",  # Specify Markdown format
    license="GPL-3.0",
    keywords="ML",
    url="https://github.com/WalidGharianiEAGLE/mdpdroi",

    # Dependencies
    python_requires='>=3.7',
     # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)