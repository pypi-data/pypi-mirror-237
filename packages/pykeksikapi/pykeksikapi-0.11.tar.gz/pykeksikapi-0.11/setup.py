from setuptools import setup, find_namespace_packages, find_packages


#with open('README.md', "r") as readme_file:
    #readme = readme_file.read()

requirements = ['aiohttp', 'typing', 'pydantic']

setup(
    name="pykeksikapi",
    version="0.11",
    author="unneccessaryss",

    description="This library is needed for working with api.keksik.io. It provides convenient tools for processing the API of this website.",
    #long_description=readme,
    #long_description_content_type="text/markdown",
    url="https://github.com/unnecessaryss/pykeksikapi",

    packages=find_namespace_packages(),
    install_requires=requirements,
    python_requires=">=3.9",

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
