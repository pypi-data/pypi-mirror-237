from setuptools import setup, find_packages

setup(
    name='SelSensei',
    version='0.0.1',
    author='Miles Read',
    author_email='readmiles00@gmail.com',
    description='Lightweight Selenium wrapper',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
