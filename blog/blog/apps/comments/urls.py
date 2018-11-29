# -*- coding:utf8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comments/$', views.ArticleCommentView.as_view()),  # 查询文章评论数据
    url(r'^post_comments/$', views.PostArticleCommentView.as_view()),  # 新增文章评论数据
]

