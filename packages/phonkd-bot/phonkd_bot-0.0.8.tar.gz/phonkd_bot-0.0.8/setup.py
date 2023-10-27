from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = 'A framework that makes discord bot programming easy'

with open("README.md", "r") as f:
    long_description = f.read()

# Setting up
setup(
    name="phonkd_bot",
    version=VERSION,
    author="Phonki",
    author_email="<phonkibusiness@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["discord", "asyncio"],
    keywords=['python', 'discord'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ]
)