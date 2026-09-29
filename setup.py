from setuptools import setup, find_packages

setup(
    name='FactorySymPy',
    version='0.1.0',
    description='Intelligent factory simulation using SymPy',
    author='Rat-mon',
    packages=find_packages(),
    install_requires=[
        'sympy>=1.11',
        'numpy>=1.20.0',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
