from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()


def main():
    pkg_setup = {
        'name': 'django-web3-auth',
        'version': '0.0.1',
        'description': 'Django authentication using an Ethereum wallet',
        'long_description': LONG_DESCRIPTION,
        'long_description_content_type': 'text/markdown',
        'author': 'Teodor Ivanov',
        'author_email': 'tdrivanov@gmail.com',
        'packages': find_packages(exclude=['*tests*']),
        'python_requires': '>=3.9',
        'install_requires': [
            'eth_utils>=1.10.0',
            'Django>=3.2.0',
            # workaround for python 3.11 with pycryptodome (due to ethereum package switch to web3 package)
            'pycryptodome>=3.15.0',
            'py-ecc>=5.2.0',
            'rlp>2.0.0',
        ],
        'extras_require': {},
        'include_package_data': True,
        'license': 'MIT',
        'project_urls': {
            'Source': 'https://github.com/krilarite/django-web3-auth',
        },
    }
    setup(**pkg_setup)


if __name__ == '__main__':
    main()
