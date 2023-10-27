import setuptools

setuptools.setup(
    name = "mt_testpackage_python",
    version = "0.0.1",
    author = "author",
    author_email = "heinz.werner73@gmx.de",
    description = "my very first PyPI project",
    url = "https://pypi.org/project/mt_testpackage_python",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(exclude="tests"),
    python_requires = ">=3.6"
)
