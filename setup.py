import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="src",
    version="0.0.1",
    author="manan-bedi2908",
    author_email="mananbedilps@gmail.com",
    description="It is the implementation of ANN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manan-bedi2908/ANN_Implementation",
    project_urls={
        "Bug Tracker": "https://github.com/manan-bedi2908/ANN_Implementation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)