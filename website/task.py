# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: magic
"""
from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the default Django settings mudule for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('website')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

