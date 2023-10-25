from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyapks",
    version="0.0.1-b",
    description="Apk Downloader is a Python module that allows you to download Android APK files using alternative sources such as Aptoide and ApkPure.",
    author="09u2h4n",
    author_email="09u2h4n.y1lm42@gmail.com",
    packages=find_packages(),
    install_requires=["requests", "tqdm", "bs4"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)