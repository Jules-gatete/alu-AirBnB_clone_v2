#!/usr/bin/python3
""" 
Fabric script that creates and distributes an archive to your web servers 
"""
from fabric.api import env, local, run, put
from os.path import exists
from datetime import datetime

env.hosts = ["54.227.78.227", "34.229.215.10"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        get_date = datetime.now().strftime("%Y%m%d%H%M%S")
        if exists("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(get_date)
        # Add my_index.html to the web_static folder
        local("echo '<html><head></head><body>My Index Page</body></html>' > web_static/my_index.html")
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path = "/data/web_static/releases/{}/".format(no_ext)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except:
        return False

def deploy():
    """ Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:     
        return False
    return do_deploy(archive_path)

def deploy_local():
    """Creates and deploys a new version locally"""
    return deploy()

# Call the deploy_local function when the script is executed directly
if __name__ == "__main__":
    deploy_local()
