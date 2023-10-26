from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pycxsim',
    version="0.1.5",
    license="MIT",
    author="Aaron Tamte",
    author_email="aaron2804@gmail.com",
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,  # List of dependencies
    description="PyCxsim is a framework to simulate computational agents in a confined environment.",
    url="https://github.com/Aatamte/PyCxsim",
    keywords=["Artificial Intelligence", "Simulation"],
    package_dir={'': 'src'},
    package_data={
        'cxsim': ['prompts/*.txt', 'gui/assets/*.ico'],
    },
    # other parameters...
)
