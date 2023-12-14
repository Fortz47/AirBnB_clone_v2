#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function"""

from fabric.api import local, run, put, env
from datetime import datetime
import os
import re

env.user = "ubuntu"
env.hosts = ['18.234.130.161', '54.157.184.77']


def do_pack():
    """creates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_name = f"versions/web_static_{date}.tgz"
    print(f"Packing web_static to {archive_name}")
    local('mkdir -p versions')
    result = local(f"tar -cvzf {archive_name} web_static")
    if result.return_code == 0:
        return archive_name
    return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_tgz = re.search('(web_static_.*.tgz$)', archive_path).group(1)
        archive = archive_tgz[:-4]
        run(f'mkdir -p /data/web_static/releases/{archive}')
        extract_cmd = f'tar -xz \
        -C /data/web_static/releases/{archive} \
        -f /tmp/{archive_tgz}'
        run(extract_cmd)
        run(f'rm /tmp/{archive_tgz}')

        run(f'mv /data/web_static/releases/{archive}/web_static/* \
        /data/web_static/releases/{archive}/')

        run(f'rm -rf /data/web_static/releases/{archive}/web_static')
        run('rm /data/web_static/current')
        path_target = f'/data/web_static/releases/{archive}'
        run(f'ln -s {path_target} /data/web_static/current')
    except Exception as e:
        print(e)
        return False
    print("New version deployed!")
    return True


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path:
        status = do_deploy(archive_path)
        return status
    return False


def do_clean(number=0):
    """deletes out-of-date archives, using the function"""
    archives_local = os.listdir("versions")
    archives_remote = run('ls /data/web_static/releases').split()
    archives_remote.remove('test')
    number = 1 if number == 0 else int(number)
    count_local = len(archives_local) - number
    count_remote = len(archives_remote) - number
    if count_local > 0:
        archives_local.sort()
        for item in archives_local[number:]:
            local(f'rm versions/{item}')

    if count_remote > 0:
        archives_remote.sort()
        for item in archives_remote[number:]:
            run(f'rm /data/web_static/releases/{item}')
