from setuptools import setup, find_packages

setup(
    name="jindo-aws-py",
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3'
    ]
)
