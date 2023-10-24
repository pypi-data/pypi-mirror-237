#python3 setup.py sdist ###bdist bdist_wheel

# For testing
#python3 -m twine upload --repostitory testpypi dist/*
#python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps multiio

# For release
#python3 -m twine upload dist/*
#pip install multiio


long_description = ""

files = ["README.md", "../README.md"]
for file in files:
    try:
        with open(file, "r") as fh:
            long_description = fh.read()
    except IOError:
        pass
if long_description == "":
    raise IOError("File README.md couldn't be found/read")

from setuptools import setup, find_packages
setup(
    name='multiio',
    packages=find_packages(),
    version='1.0.0',
    license='MIT',
    description='Library to control Multi-IO Automation Card',
    long_description=long_description,
    author='Sequent Microsystems',
    author_email='olcitu@gmail.com',
    url='https://sequentmicrosystems.com',
    keywords=['industrial', 'raspberry', 'power', '4-20mA', '0-10V', 'optoisolated'],
    install_requires=[
        "smbus2",
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    )
