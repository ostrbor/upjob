from fabric.api import local, task
from settings import RESOURCES_DIR


@task
def build():
    local('docker build -t upjob .')


@task
def run():
    local(f'docker run -v {RESOURCES_DIR}:/usr/src/app/db upjob')
