"""定义learnig_log的URL模式"""
from django.contrib import admin
from django.conf.urls import url, re_path
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]
