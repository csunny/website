#!coding:utf-8

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mongoengine import *


class Post(Document):
    meta = {
        'collection': 'post_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()
    text = StringField()
    created_date = DateTimeField(default=timezone.now)
    publish_date = DateTimeField()

    def publish(self):
        self.publish_date = timezone.now()
        self.save()



# class Post(models.Model):
#     author = models.ForeignKey(User)
#     title = models.CharField(max_length=200,verbose_name='文章标题')
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
# 	class Meta:
# 		verbose_name = "文章"
# 		verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.title
