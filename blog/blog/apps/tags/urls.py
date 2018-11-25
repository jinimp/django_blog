# -*- coding:utf8 -*-

"""

"""
from django.conf.urls import url
from tags import views

urlpatterns = [
    url(r'^tag/$', views.tag_template),  # 返回一个空的标签模板
    url(r'^tags/$', views.TagView.as_view()),  # 查询标签数据
    url(r'^tags_articles/$', views.ArticleTagView.as_view()),  # 查询标签数据
]