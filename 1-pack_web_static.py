#!/usr/bin/python3
from datetime import datetime
from fabric.api import * 
from os.path import isdir 


def do_pack():
    try:
       get_date = datetime.now().strftime("%Y%m%d%H%M%S")
       if isdir("versions") is False:
         local("mkdir versions")
       filename = "versions/web_static_{}.tgz".format(get_date)
       local("tar -cvzf {} web_static".format(filename))
       return filename
    except:
       return None 