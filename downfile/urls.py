'''
Created on 2013-10-24

@author: heruilong
'''
from django.conf.urls import patterns, url
from downfile import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)