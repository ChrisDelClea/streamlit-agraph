import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# python setup.py sdist bdist_wheel
# python -m twine upload  dist/*

setuptools.setup(
    license="MIT",
    name="streamlit-agraph",
    version="0.0.45",
    author="Christian Klose",
    author_email="chris.klose@gmx.net",
    description="Interactive Graph Vis for Streamlit.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChrisChross/streamlit-agraph",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "networkx >= 2.5",
        "rdflib >= 6.0.2",
    ],
)
