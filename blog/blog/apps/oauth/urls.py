# -*- coding:utf8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_template),  # 返回登录页面模板
    url(r'^qq/authorization/$', views.QQAuthURLView.as_view()),  # 获取qq登录页面链接
    url(r'^qqlogin/$', views.oauth_callback),  # 返回回调页面模板
    url(r'^qq/user/$', views.QQAuthUserView.as_view()),  # 用户扫码登录后回调处理
]
