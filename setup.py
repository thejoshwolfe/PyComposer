from distutils.core import setup

import src.composer.composer

setup(
    name=composer.__name__,
    version=composer.__author__,
    long_description=composer.__doc__,
    author_email=composer.__email__,
    url='http://github.com/thejoshwolfe/PyComposer/',
    py_modules=("composer",)
)

