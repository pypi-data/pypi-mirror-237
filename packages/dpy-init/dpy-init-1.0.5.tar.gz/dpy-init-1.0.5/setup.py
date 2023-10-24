from setuptools import setup, find_packages

# Read the contents of your README.md file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dpy-init',
    version='1.0.5',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'dpy-init = dpy_init.dpy_init:dpy_init',
        ],
    },
    long_description=long_description,  # Set the long description to the contents of README.md
    long_description_content_type='text/markdown',  # Specify the content type of the README
)
