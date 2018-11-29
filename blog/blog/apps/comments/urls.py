# -*- coding:utf8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comments/$', views.ArticleCommentView.as_view()),  # 查询文章详情数据
]

