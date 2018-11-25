# -*- coding:utf8 -*-

"""

"""
from django.conf.urls import url
from categorys import views

urlpatterns = [
    url(r'^categorys/$', views.CategoryView.as_view()),  # 查询分类的数据
]