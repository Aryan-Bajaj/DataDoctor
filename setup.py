from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DataDoctor',
    version='1.0.4',
    author='Aryan Bajaj',
    author_email='aryanbajaj104@email.com',
    description="A Python package for data cleaning and preprocessing.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'fuzzywuzzy',
        'python-Levenshtein',
        'chardet'
    ],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Data Analyst and Data Engineers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent and Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='data cleaning preprocessing machine learning pandas numpy scikit-learn fuzzywuzzy data normalization',
)