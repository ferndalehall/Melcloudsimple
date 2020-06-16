import pathlib
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setuptools.setup(
    name="Melcloudsimple",
    version="0.0.1",
    author="John Pickford",
    author_email="John.pickford@ferndale-hall.co.uk",
    description="A simple MELCloud access package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
	license='MIT',
	project_urls={
    	'Source': 'https://github.com/ferndalehall/Melcloudsimple',
    	'Tracker': 'https://github.com/ferndalehall/Melcloudsimple/issues',
	},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["Melcloudsimple"],
	package_dir={"Melcloudsimple":'src/Melcloudsimple'},
	package_data = {"Melcloudsimple": ["images/*.svg", "scripts/*", "example/Melprog.py"],},
	depends=['requests']

)
