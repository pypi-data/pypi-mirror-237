

import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
name="psgup",
version="2.4",
author="PySimpleSoft",
author_email="someone@somewhere.com",
install_requires=["PySimpleGUI"],
description="Application distribution via PyPI",
long_description=readme(),
long_description_content_type="text/markdown",
license='Free To Use But Restricted',
keywords="PySimpleGUI Application Distribution",
url="https://github.com/PySimpleGUI",
# packages=setuptools.find_packages(),
packages=["psgup"],
python_requires=">=3.6",
classifiers=[
"Development Status :: 5 - Production/Stable",
"Intended Audience :: Developers",
"License :: Free To Use But Restricted",
"Operating System :: OS Independent",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.6",
"Programming Language :: Python :: 3.7",
"Programming Language :: Python :: 3.8",
"Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10",
"Programming Language :: Python :: 3.11",
"Programming Language :: Python :: 3.12",
"Programming Language :: Python :: 3.13",
"Topic :: Multimedia :: Graphics",
"Topic :: Software Development :: User Interfaces",
"Development Status :: 2 - Pre-Alpha",
"Development Status :: 3 - Alpha",
],
package_data={"": ["*.ico", "LICENSE.txt", "README.md"]},
entry_points={'gui_scripts': [
"psgup=psgup.psgup:main",
    ]
    },
)

