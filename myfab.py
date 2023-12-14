#!/usr/bin/python3

"""a Fabric script that generates a .tgz archive from the contents of the web_static folder"""


from fabric.api import env, run, put, cd

env.user = "ubuntu"
env.hosts = ['18.234.130.161', '54.157.184.77']

def do_copy(file):
    """copy from local to remote"""
    run('mkdir -p /home/ubuntu/operations')

    put(file, '/home/ubuntu/operations/', mode=755)

def do_exec(File):
    """execute a remote file"""
    with cd('/home/ubuntu/operations/'):
        me = run(File)
        print(me, type(me))
        new = me.split()
        print(new)
