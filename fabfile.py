# -*- coding: utf-8 -*-

u"""
.. module:: fabfile
Be aware, that becaus fabric doesn't support py3k You need to execute this
particular script using Python 2.
"""

from fabric.api import cd
from fabric.api import env
from fabric.api import run

env.user = 'root'
env.hosts = ['plantingjs.org']
env.forward_agent = True


def update():
    u"""Function defining all steps required to properly update application."""

    with cd('/var/www/plantingjs_org'):
        run('git pull')
        run('git checkout master')
        run('npm cache clear')
        run('rm -rf ./node_modules')
        run('npm install')
        run('gulp build')

    run('service apache2 restart')
