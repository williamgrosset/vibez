from setuptools import setup, find_packages

setup(
    name="yaink",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyperclip"
    ],
    entry_points={
        "console_scripts": [
            "yaink=yaink.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)