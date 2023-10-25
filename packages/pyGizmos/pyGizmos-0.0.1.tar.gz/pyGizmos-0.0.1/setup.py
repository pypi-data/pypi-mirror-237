import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="pyGizmos",
    version="0.0.1",
    author="GrkDev",
    author_email="thedevgrk@gmail.com",
    description="This Python package brings you quick, easy, and fun tools to help you with Python development.",
    long_description=long_description, # don't touch this, this is your README.md
    long_description_content_type="text/markdown",
    url="https://replit.com/@GrkDev/pyGizmos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)