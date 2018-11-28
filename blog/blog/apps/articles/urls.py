# -*- coding:utf8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    url(r'^article/$', views.article_template),  # 文章详情模板页,返回一个空的模板
    url(r'^articles/$', views.ArticleDetailView.as_view()),  # 查询文章详情数据

    url(r'^article_list/$', views.article_list_template),  # 文章列表模板页,返回一个空的模板
    url(r'^article_lists/$', views.ArticleListView.as_view()),  # 查询文章列表页数据

    url(r'^lastest/$', views.LastestArticleView.as_view()),  # 查询最新发表的前三篇文章

    url(r'^search/$', views.search_template),  # 文章标题搜索,返回搜索页面

    url(r'^rank/$', views.ArticleClickRankView.as_view())  # 文章点击排行
]

# 搜索视图集
router = DefaultRouter()
router.register('articles/search', views.ArticleSearchViewSet, base_name='articles_search')
urlpatterns += router.urls
