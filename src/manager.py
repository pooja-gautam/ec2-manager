# --help Show msg and exit
# instances - Commands for instances [list, snapshot, start, stop]
# snapshots - Commands for snapshots []
# volumes - Commands for volumes

import boto3
import click

session = boto3.Session(profile_name='aws_practice')
ec2 = session.resource('ec2')


@click.command()
def list_instances():
    """ List all instances """
    for i in ec2.instances.all():
        print(", ".join((
            i.id, i.instance_type, i.placement['AvailabilityZone'], i.state['Name'], i.public_dns_name))
        )


if __name__ == '__main__':
    list_instances()
