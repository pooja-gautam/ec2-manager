from setuptools import setup

setup(
    name="Ec2-manager-2020",
    version="0.1",
    author="Pooja Gautam",
    description="Script that manages AWS EC2 snapshots.",
    license="GPLv3+",
    packages=["src"],
    install_requires=["click", "boto3"],
    entry_points='''
        [console_scripts]
        ec2_snapshots=src.manager:cli
    '''
)