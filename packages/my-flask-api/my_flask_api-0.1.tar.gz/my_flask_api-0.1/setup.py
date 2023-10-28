from setuptools import setup, find_packages

setup(
    name='my_flask_api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'my_flask_api=my_flask_api.app:main',
        ],
    },
)
