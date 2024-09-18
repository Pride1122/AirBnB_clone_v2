#!/usr/bin/python3
"""Module that creates an archive using fabric"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packs the contents of the web_static folder into a tgz archive."""
    try:
        local("mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(now)
        local("tar -czvf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except Exception as e:
        return None
