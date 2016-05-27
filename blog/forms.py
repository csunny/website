#!/usr/bin/env python
#！coding: utf-8
'''
@author: magic
'''
from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text',)