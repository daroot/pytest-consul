from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='pytest-consul',
    version='0.0.0',
    description='pytest plugin with fixtures for testing consul aware apps',
    long_description=readme(),
    url='http://github.com/daroot/pytest-consul',
    author='Dan Root',
    author_email='rootdan+pypi@gmail.com',
    license='WTFPL',

    packages=find_packages(),
    install_requires=['pytest'],
    tests_require=['pytest-flake8', 'requests', 'pytest-cov'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',

    entry_points={
        'pytest11': [
            'consul = pytest_consul.plugin',
        ],
    },

    keywords=['pytest', 'consul'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
