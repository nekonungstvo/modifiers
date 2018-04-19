from distutils.core import setup

from setuptools import find_packages

setup(
    name='modifiers',
    version='0.0.0',
    packages=find_packages(exclude=["tests"]),
    url='https://konungstvo.ru',
    license='GPLv3',
    author='xunto',
    author_email='',
    description='',
    entry_points={
        "console_scripts": [
            "modifiers=modifiers.aiohttp_controller.app:run"
        ],
    },
    install_requires=[
        "motor", "pytest-asyncio", "pydantic", 'aiohttp'
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    }
)
