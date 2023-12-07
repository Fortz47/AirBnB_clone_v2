#!/usr/bin/python3
"""
    Distributes an archive to your web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['52.72.14.202', '18.204.9.164']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None


def do_deploy(archive_path):
    """
    Deploys an archive to a server
    """
    if exists(archive_path) is False:
        return False
    try:
        file_N = archive_path.split("/")[-1]
        n = file_N.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, n))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_N, path, n))
        run('rm /tmp/{}'.format(file_N))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, n))
        run('rm -rf {}{}/web_static'.format(path, n))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, n))
        run('chmod -R 755 /data/')
        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False
