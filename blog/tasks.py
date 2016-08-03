# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: magic
"""
from __future__ import absolute_import
from celery import shared_task


@shared_task
def test(param):
	return 'the test task executed with argument "%s" ' %param

