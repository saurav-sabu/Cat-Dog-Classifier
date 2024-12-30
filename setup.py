from setuptools import setup, find_packages

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="Dog_Cat_Classifier",
    version="0.0.0",
    author="Saurav Sabu",
    author_email="saurav.sabu9@gmail.com",
    description="A small package to classify dogs and cats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saurav-sabu/Cat-Dog-Classifier",
    project_urls={
        "Bug Tracker": "https://github.com/saurav-sabu/Cat-Dog-Classifier/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)