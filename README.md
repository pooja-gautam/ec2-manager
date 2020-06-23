# ec2-manager
Script that lets you start/stop AWS EC2 instances and take snapshots of attached volumes.

# System requirements
This project requires Python 3, Pipenv and AWS Cli. 

#Configuring
ec2-manager uses aws configurations created by AWS on the system. 
for eg: ```aws configure --profile {profile name}```
or add the profile's configs to your aws credentials file.

# Running script
```pipenv run python src/manager.py <command> <--project=PROJECT>```

*command* is instances, snapshots, volumes
*project* is optional

Run with --help to get help for each command. 

## Installing

To install this tool, run ```python setup.py install```

To generate a wheel, ```python setup.py bdist_wheel```
Install the generated wheel using pip.

Run with: ```ec2_snapshots <command> <project>```
