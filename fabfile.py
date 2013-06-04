from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['recipecenter.in']
SUPERVISOR_DIR = 'recipecenter/supervisord.conf/'
env.port = 49169


def make_supervisor_conf():
    put('recipecenter' % {'supervisor_dir': SUPERVISOR_DIR})


def test():
    with settings(warn_only=True):
        result = local('./manage.py test recipecenter', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()


def deploy():
    code_dir = '/home/agiliq/recipecenter'
    make_supervisor_conf()

    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:agiliq/recipecenter.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run(" pip install -r requirements.txt")
        run("cp local_settings.py-dist local_settings.py")
        run("python manage.py syncdb --migrate --noinput")
        run("supervisorctl restart recipecenter:gunicorn_recipecenter")
