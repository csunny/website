#!/usr/bin/env python
<<<<<<< HEAD
# coding: utf-8
"""
@author: magic
"""
=======
#！coding: utf-8
'''
@author: magic
'''
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222

from django.conf.urls import patterns, include, url
from blog.views import *

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^post_list/$', post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', post_detail, name="post_detail"),
	url(r'^post/new/$', post_new, name="post_new"),
	url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name="post_edit"),
	url(r'^drafts/$', post_draft_list, name="post_draft_list"),
	url(r'^post/(?P<pk>[0-9]+)/publish/$', post_publish, name="post_publish"),
	url(r'^post/(?P<pk>\d+)/ remove/$', post_remove, name="post_remove"),
)

=======
    url(r'^$', post_list,name='post_list'),
	url(r'^post/(?P<pk>\d+)/$',post_detail,name="post_detail"),
	url(r'^post/new/$',post_new,name="post_new"),
	url(r'^post/(?P<pk>\d+)/edit/$',post_edit,name="post_edit"),
	url(r'^drafts/$',post_draft_list,name="post_draft_list"),
	url(r'^post/(?P<pk>[0-9]+)/publish/$',post_publish,name="post_publish"),
	url(r'^post/(?P<pk>\d+)/ remove/$',post_remove,name="post_remove"),



)
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
