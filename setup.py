from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pynotice',
    version='0.0.1',
    author='shaoeric',
    author_email='shaoeric@foxmail.com',
    url='https://github.com/shaoeric/pynotice',
    description="notice by sound or email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        "": ["*.wav", "*.md", "*.txt"]
    },
    include_package_data = True,
    install_requires=['simpleaudio==1.0.2', 'zmail==0.2.5', 'filetype==1.0.5'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)