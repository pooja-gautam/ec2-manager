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
def cli():
    """ Manages instances and snapshots """


@cli.group('instances')
def instances():
    """ Returns all instances """


@cli.group('volumes')
def volumes():
    """ Manages all volumes """


@cli.group('snapshots')
def snapshots():
    """ Manages snapshots """


@snapshots.command('list')
@click.option('--project', default=None,
              help='Only snapshots for project (tag Project:<name>)')
def list_snapshots(project):
    """ List EC2 volume snapshots """
    instances = get_instances(project)
    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(", ".join((s.id, v.id, i.id, s.state, s.progress, s.start_time.stfrtime("%c"))))
    return


@snapshots.command('create')
@click.option('--project', default=None,
              help='Only snapshots for project (tag Project:<name>)')
def create_snapshots(project):
    """ List EC2 volume snapshots """
    instances = get_instances(project)
    for i in instances:
        for v in i.volumes.all():
            if i.state['Name'] != 'Stopped':
                print(f'Stopping instance {i.id} before creating snapshot')
                i.stop()
                i.wait_until_stopped()
            print(f'Creating snapshot of volume {v.id}')
            v.create_snapshot(Description=' Created by Ec2-manager ')
            i.start()
    print("Job's done!")
    return


@volumes.command('list')
@click.option('--project', default=None,
              help='Only volumes for project (tag Project:<name>)')
def list_volumes(project):
    """ List EC2 volumes """
    instances = get_instances(project)
    for i in instances:
        for v in i.volumes.all():
            print(", ".join((v.id, i.id, v.state, str(v.size) + "GiB", v.encrypted and "Encrypted" or "Not Encrypted")))


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
    cli()
