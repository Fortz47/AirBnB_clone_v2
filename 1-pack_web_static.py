#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive
from the contents of the web_static folder"""


from fabric.api import local
from datetime import datetime

# env.user = "ubuntu"
# env.hosts = ['18.234.130.161', '54.157.184.77']


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
