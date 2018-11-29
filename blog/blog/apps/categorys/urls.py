# -*- coding:utf8 -*-

"""

"""
from django.conf.urls import url
from categorys import views

urlpatterns = [
    url(r'^categorys/$', views.CategoryView.as_view()),  # 查询分类的数据

    url(r'^nav_dropdown/$', views.NavDropdownView.as_view()),  # 导航栏下拉标签所有信息
]