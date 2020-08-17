import os

from invoke import task


@task
def clean_dist(c):
    c.run(f'rm -rf dist')


@task(pre=[clean_dist])
def build(c):
    with c.cd('sources'):
        dist_dir = os.path.join(os.getcwd(), 'dist')
        c.run(f'python setup.py sdist --dist-dir {dist_dir}')
