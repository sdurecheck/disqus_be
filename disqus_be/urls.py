"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from core_app.api import CommentResource

comment_resource = CommentResource()

urlpatterns = patterns('',
    url(r'^api/v1/',  include(comment_resource.urls)),
)
