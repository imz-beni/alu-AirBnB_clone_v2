#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to the web servers, using the function do_deploy.
"""
from os.path import exists
from fabric.api import env, put, run
from io import StringIO

env.hosts = ['3.82.176.167', '98.94.20.97']


def do_deploy(archive_path):
    """Distributes an archive to the web servers.

    Args:
        archive_path (str): the path of the archive to deploy.

    Returns:
        bool: True if all operations have been done correctly,
        otherwise False.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/{}'.format(file_name))
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        nginx_conf = (
            'server {\n'
            '    listen 80 default_server;\n'
            '    listen [::]:80 default_server;\n'
            '    root /var/www/html;\n'
            '    index index.html index.htm;\n'
            '    server_name _;\n\n'
            '    location /hbnb_static/ {\n'
            '        alias /data/web_static/current/;\n'
            '        index index.html index.htm;\n'
            '    }\n\n'
            '    location / {\n'
            '        try_files $uri $uri/ =404;\n'
            '    }\n'
            '}\n'
        )
        put(StringIO(nginx_conf), '/tmp/nginx_hbnb.conf')
        run('sudo mv /tmp/nginx_hbnb.conf /etc/nginx/sites-available/default')
        run('sudo ln -sf /etc/nginx/sites-available/default'
            ' /etc/nginx/sites-enabled/default')
        run('sudo service nginx restart')
        print("New version deployed!")
        return True
    except Exception:
        return False
