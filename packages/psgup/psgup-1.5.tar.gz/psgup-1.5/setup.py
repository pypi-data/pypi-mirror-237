import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="psgup",
    version="1.5",
    author="PySimpleSoft",
    author_email="someone@somewhere.com",
    # install_requires=['PySimpleGUI>=5',],     # TODO uncomment when PSG5 posts
    description="Quick uplaod to PyPI",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='Free To Use But Restricted',
    # keywords="GUI UI PySimpleGUI tkinter psgresizer base64 resize",
    # url="https://github.com/PySimpleGUI",
    # packages=setuptools.find_packages(),
    packages=['psgup'],
    python_requires='>=3.6',
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
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: User Interfaces",
    ],
    # package_data={"": ["*.ico", "LICENSE.txt", "README.md"]},
    entry_points={'gui_scripts': ['psgup=psgup.psgup:main',],},
)