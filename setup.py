import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="benford_law",
    version="0.1.1",
    author="Rafael Mata",
    author_email="rafaelmata357@gmail.com",
    description="A python tool to calculate the Benford´s Law from a dataset or image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelmata357/benford",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['wheel']
)