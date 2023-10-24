"""The setup script."""

from setuptools import setup, find_packages

#with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = []
test_requirements = []

setup(
    author="""Anas Filali Razzouki, Mounim El Yacoubi , Dijana Petrovska, Laetitia Jeancolas, Ahmed Zaiou and Gaëtan Brison""",
    author_email='engineer.hi.paris@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="""classification model using image time series for parkinson detection""",
    install_requires=["numpy", "pandas", "scipy", "scikit-learn", "torch", "pytorch"],
    license="MIT license",
    keywords='parkinson-detect',
    name='parkinson-detect',
    packages=find_packages(include=['parkinson-detect', 'parkinson-detect.*']),
    include_package_data=True,

    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hi-paris/parkinson-detect',
    version='0.0.1',
    zip_safe=False,
)
