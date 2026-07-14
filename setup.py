# coding: utf-8

from setuptools import setup, find_packages

NAME = "asposehtmlcloud"
VERSION = "26.7.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10",  "certifi", "pyopenssl", "urllib3[secure]", "python-dateutil", "requests[security]"]

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setup(
    name=NAME,
    version=VERSION,
    description='Aspose.HTML for Cloud Python SDK',
    author='Aspose',
    author_email='alexander.makogon@aspose.com',
    url="https://github.com/aspose-html-cloud/aspose-html-cloud-python",
    license='MIT',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=[
	    "html2pdf",
		"epub2pdf",
		"md2html",
		"html2md",
		"html2img",
		"html2xps",
		"epub2xps",
		"convert"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
	long_description_content_type="text/markdown"
)
