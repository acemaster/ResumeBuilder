# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

def get_image_path(instance,filename):
    return 'profile/{0}'.format(filename)

class PersonalProfile(models.Model):
	name = models.CharField(max_length=100,primary_key=True)
	quote = models.CharField(max_length = 100)
	emailId = models.CharField(max_length = 100)
	description = models.TextField()
	profilePicture=models.ImageField(upload_to=get_image_path,null=True,blank=True)
	linkedIn = models.CharField(max_length=100)
	twitter = models.CharField(max_length = 100)
	github = models.CharField(max_length= 100)
	def __unicode__(self):
		return self.name


class Section(models.Model):
	id=models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	content = RichTextField()
	def __unicode__(self):
		return str(self.id)
