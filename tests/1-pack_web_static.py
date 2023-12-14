#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive
"""
import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Compresses the web_static folder into a .tgz archive"""
    try:
        day = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fileName = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_static".format(fileName))
        return fileName
    except FileNotFoundError:
        return None
