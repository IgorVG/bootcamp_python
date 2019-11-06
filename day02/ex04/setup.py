import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ai42", # Replace with your own username
    version="1.0.0",
    author="igarbuz",
    author_email="igarbuz@student.42.fr",
    description="package containing ft_progress and log functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/igarbuz/day02/ex04",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)