from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Find words or sentences containing or starting/ending with a substring'
LONG_DESCRIPTION = 'A package that allows to Find words or sentences containing or starting/ending with a substring, from text file where sentences are separated by new lines'

# Setting up
setup(
    name="nufi",
    version=VERSION,
    author="Shck Tchamna",
    author_email="<tchamna@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'nufi', 'sentences extraction', 'word extraction', 'word finder', 'sentence finder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)