#!coding:utf-8

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

<<<<<<< HEAD

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200, verbose_name='文章标题')
=======
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200,verbose_name='文章标题')
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

<<<<<<< HEAD
=======

>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
    def publish(self):
        self.published_date = timezone.now()
        self.save()

	class Meta:
		verbose_name = "文章"
		verbose_name_plural = verbose_name

<<<<<<< HEAD
=======


>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
    def __unicode__(self):
        return self.title
