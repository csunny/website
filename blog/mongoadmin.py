#!/usr/vin/env python
# -*- coding:utf-8 -*-
"""
  @date = ''
__author__ = 'magic'
"""
from mongonaut.sites import MongoAdmin

from blog.models import Post
Post.mongoadmin = MongoAdmin
