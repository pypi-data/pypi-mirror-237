import setuptools

setuptools.setup(
    name="alida-notebook-utils",
    version="0.0.1",
    author="Alida research team",
    author_email="engineering-alida-lab@eng.it",
    description="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = [
        "ds-io-utilities",
        "alida-arg-parser",
        "file-io-utilities",
        "pandas"
        ],
)
