# ec2-manager
Script that lets you manage AWS EC2 instances and take snapshots 

# System requirements
This project requires Python 3 and pipenv. 

#Configuring
ec2-manager uses aws configurations created by AWS on the system. 
for eg: ```aws configure --profile {profile name}```
or add the profile's configs to your aws credentials file.

# Running script
```pipenv run python src/manager.py <command> <--project=PROJECT>```

*command* is start, stop, list, snapshots
*project* is optional

