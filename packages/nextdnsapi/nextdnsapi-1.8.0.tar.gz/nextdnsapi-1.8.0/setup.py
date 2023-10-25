from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
# wU2A6AagBtZSyEm
setup(
    name="nextdnsapi",
    packages=find_packages(include=["nextdnsapi"]),
    version="1.8.0",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="I was getting increasingly frustrated with NextDNS's lack of API. I wanted to manage things on the fly. So, I did the most logical thing. I built a python script (library-to-be) to control my NextDNS account. I decided to make it public because why not?",
    author_email="nextdns@ramzihijjawi.me",  # Type in your E-Mail
    url="https://github.com/rhijjawi/NextDNS-API",  # Provide either the link to your github or to your website
    download_url="https://github.com/rhijjawi/NextDNS-API/archivev1-7-0.tar.gz",  # I explain this later on
    keywords=["NEXTDNS", "API", "REQUESTS"],  # Keywords that define your package best
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: 3.9",
	"Programming Language :: Python :: 3.10",
    ],
)
