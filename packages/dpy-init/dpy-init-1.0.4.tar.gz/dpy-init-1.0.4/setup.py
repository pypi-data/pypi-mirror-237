from setuptools import setup, find_packages

setup(
    name='dpy-init',
    version='1.0.4',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'dpy-init = dpy_init.dpy_init:dpy_init',
        ],
    },
)
