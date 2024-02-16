#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo using the function do_pack.
"""
import fabric.api as fab
from datetime import datetime
import os

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    The archive name is based on the current date and time.
    Returns the path to the created archive.
    """
    try:
        date_str = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(date_str)
        fab.local("mkdir -p versions")
        fab.local("tar -cvzf versions/{} web_static".format(archive_name))
        return os.path.join("versions", archive_name)
    except Exception as e:
        return None

if __name__ == "__main__":
    do_pack()

