from setuptools import setup, find_packages

setup(
    name='naru',
    version='0.0.1',
    description='PYPI tutorial package creation written by TeddyNote',
    author='psw109',
    author_email='psw109@gmail.com',
    url='https://github.com/teddylee777/teddynote',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['teddynote', 'teddylee777',
              'python datasets', 'python tutorial', 'pypi'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
