from distutils.core import setup

setup(
    #Application Name
    name="rebrand_ossim",

    #Version number (initial)
    version="0.1.0",

    #Application author details
    author="Indika Maligaspe",
    author_email="indikamaligasp@securmatic.com",

    #packages

    #details

    #license="LICENSE.txt",

    description="Rebrand ossim sensor and web UI"

    #long_description=open("README.txt").read(),

    #Dependent packages (distribution)
    install_requires=[
        "PyYAML>=3",
        "pytest>=3"
    ],

)
