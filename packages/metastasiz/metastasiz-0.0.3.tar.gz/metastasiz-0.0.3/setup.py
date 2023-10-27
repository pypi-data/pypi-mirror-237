import setuptools

PACKAGE_NAME = "metastasiz"
VERSION = "0.0.3"
DESCRIPTION = "placeholder"

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=setuptools.find_packages(),
    extras_require={
        "dev" : ["twine>=4.0.2"],
    },
    python_requires=">=3.6",
)
