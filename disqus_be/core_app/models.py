"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5

# There we creating all needed Fields, which we will use
class Comment(models.Model):
	author = models.CharField(max_length=100)
	text = models.CharField(max_length=400)
	pub_date = models.DateField(auto_now_add=True)
	link = models.CharField(max_length=400)
	email = models.CharField(max_length=100)

	
	def __unicode__(self):
		return self.author