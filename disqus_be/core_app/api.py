"""This module contains API resource classes"""
from tastypie.resources import ModelResource
from core_app.models import Comment
from core_app import models
from tastypie.authorization import Authorization
from tastypie import fields
from core_app import utils

#This class gets all Data from Comment and append resource_name to urls.py
class CommentResource(ModelResource):
    author = fields.CharField(attribute="author")
    text = fields.CharField(attribute="text")

    class Meta:
        queryset = models.Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True
