from fabric.api import local, task
from settings import HOST_DB_DIR


@task
def build():
    local('docker build -t upjob .')


@task
def run():
    local(f'docker run -v {HOST_DB_DIR}:/usr/src/app/db upjob')
