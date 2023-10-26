from setuptools import setup,find_packages
import os
setup(
    name='pypox',
    version=str(os.getenv('__package_version__')), #type: ignore
    author='Karl Robeck Alferez',
    author_email='karlalferezfx@gmail.com',
    description='Python to javascript transpiler',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.4',
)