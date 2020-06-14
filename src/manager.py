# --help Show msg and exit
# instances - Commands for instances [list, snapshot, start, stop]
# snapshots - Commands for snapshots []
# volumes - Commands for volumes

import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='aws_practice')
    ec2 = session.resource('ec2')

    for i in ec2.instances.all():
        print(i)