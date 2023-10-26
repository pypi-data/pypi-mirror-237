from setuptools import setup

setup(
    name='http-razor',
    version='0.1',
    packages=['razor'],
    install_requires=[
        'aiofiles',
        'http-router',
        'uvicorn',
        'uvloop',
        'multidict',
        'markupsafe',
        'python-multipart',
    ],
)
