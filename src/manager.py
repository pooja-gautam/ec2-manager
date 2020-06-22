# --help Show msg and exit
# instances - Commands for instances [list, snapshot, start, stop]
# snapshots - Commands for snapshots []
# volumes - Commands for volumes

import boto3
import click

session = boto3.Session(profile_name='aws_practice')
ec2 = session.resource('ec2')


def get_instances(project=None):
    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        return ec2.instances.filter(Filters=filters)
    return ec2.instances.all()

@click.group()
def instances():
    """ Returns all instances """


@instances.command('list')
@click.option('--project', default=None,
              help='Only instances for project (tag Project:<name>)')
def list_instances(project):
    """ List all instances """
    instances = get_instances(project)
    for i in instances:
        tags = {t['Key']: t['Value'] for t in i.tags or []}
        print(", ".join((
            i.id, i.instance_type, i.placement['AvailabilityZone'], i.state['Name'], i.public_dns_name, tags.get('Project', '<no project>')))
        )


@instances.command('start')
@click.option('--project', default=None,
              help='Only instances for project (tag Project:<name>)')
def start_instances(project):
    instances = get_instances(project)
    for i in instances:
        print("Starting instances..")
        i.start()


@instances.command('stop')
@click.option('--project', default=None,
              help='Only instances for project (tag Project:<name>)')
def stop_instances(project):
    instances = get_instances(project)
    for i in instances:
        print("Stopping instances..")
        i.stop()


if __name__ == '__main__':
    instances()
