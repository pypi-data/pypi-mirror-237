import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    "numpy>=1.19.5",
]

setuptools.setup(
    name="zeusrobot",
    version="0.0.4",
    author="GlobalZeus",
    author_email="hj.park@globalzeus.com",
    description="Zeus Robot Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schooldevops/python-tutorials",
    project_urls={
        "Bug Tracker": "https://github.com/schooldevops/python-tutorials/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=install_requires,
)