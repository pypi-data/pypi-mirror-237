from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = ''
long_description=""

# Setting up
setup(
    name="sys-config-inspector",
    version=VERSION,
    author="Sai (Sai Revanth)",
    author_email="gunji.sairevanth@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    package_data={"sys-config-inspector": ["*.html"]},  # Include HTML files
    install_requires=["PyYAML >= 5.4.1","rich >= 13.4.1", "Jinja2>=3.1.2"],
    keywords=['python', 'sys-config-inspector', 'sys-config', 'inspector', 'config-inspector', 'sys config inspector'],
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
    python_requires=">=3.8",
)