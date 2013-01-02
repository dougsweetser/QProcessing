import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "QProcessing",
    version = "0.3.3",
    author = "Doug Sweetser",
    author_email = "sweetser@alum.mit.edu",
    description = ("Visual Physics App to see the math of Nature "),
    license = "Apache-2.0",
    keywords = "visual physics analytic animation quaternion processing",
    url = "http://qprocessing.atlassian.net",
    packages=['visualphysics', 'visualphysics.layout'],
    package_data={'':['processing-py.jar']},
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
)

