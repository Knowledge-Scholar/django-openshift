from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
    packages.append('django-redis-cache')
    packages.append('hiredis')

setup(name='django 1.7 on Red Hat Openshift',
    version='0.1',
    description='Django 1.7 on OpenShift Python 3.3',
    author='Your name',
    author_email='example@example.com',
    url='https://github.com/Knowledge-Scholar/django-openshift',
)
