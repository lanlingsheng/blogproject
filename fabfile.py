# -*- coding: utf-8 -*-

from fabric.api import env, run
from fabric.operations import sudo

# git 仓库
GIT_REPO = ""

# 远程登录用户名、密码、服务器地址和端口号
env.user = ""
env.password = ""

env.hosts = ['']

env.port = '22'


def deploy():
    # 代码绝对路径
    source_folder = ''

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
    """.format(source_folder))
    sudo('restart gunicorn-demo.xxx.com')
    sudo('service nginx reload')