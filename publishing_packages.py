# on terminal install 3 things globally
# pip3 install setuptools wheel twine
# to publish to pypi we need to add 3 files
# 1 setup.py
import setuptools
from pathlib import Path

setuptools.setup(
    # long_desc should be set to the content of our README.md file
    name="Sushrut", version=1.0, long_description=Path("README.md").read_text(),
    # exclude 2 dir tests , data because they dont include source code
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
# Now create readme file , contents get displayed on package homepage on pypi website
# 2 README.md // add anything
# 3 LICENSE // take template from license.com

# Generate distribution package
# python setup.py sdist bdist_wheel    sdist->Source Distribution bdist_wheel->Built Distribution
# UPLOAD
# twine upload dist/* #dist -> is the generated distribution package
# will ask for username password. Package Uploaded!
