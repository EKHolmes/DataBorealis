from setuptools import setup

# The directory containing this file


# The text of the README file
README = "DataBorealis\nAn extremely lightweight database module for Python 3.8\n\nDocumentation\n\nhelp() Function\nA simple function that prints a small, barebones tutorial. Takes no parameters.\n\nNewDB(*file_name*) class\nThe core of the DataBorealis module. Creates a new database from a .db file referenced in the single parameter.\n\nquery(*val, param*)\nUsed to search the database. The *val* parameter specifies the type of data you are searching for (name-value pair (nvp) or single value (vlu)), while the *param* parameter is the keyword you are searching for. The name of a name-value pair, or the value of a single value. Returns the value of a name-value pair, or True/False for a value, depending on whether or not the value exists.\n\ninsert(*val, param*)\nUsed to insert data into the database. Same parameters as the query() function, but the *param* parameter is the data to be inserted."

# This call to setup() does all the work
setup(
    name="databorealis",
    version="1.0.2",
    description="Localized, file-based database module.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EKHolmes/DataBorealis/",
    author="Erik Holmes",
    author_email="zv.eevee6718@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
