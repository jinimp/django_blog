"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from oauth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 后台管理员
    url(r'^', include('blog.apps.users.urls')),  # 用户
    url(r'^', include('blog.apps.oauth.urls')),  # qq登录回调地址
    url(r'^oauth/', include('blog.apps.oauth.urls')),  # qq登录
    url(r'^', include('blog.apps.articles.urls')),  # 文章
    url(r'^', include('blog.apps.categorys.urls')),  # 分类
    url(r'^', include('blog.apps.tags.urls')),  # 标签
    url(r'mdeditor/', include('mdeditor.urls')),  # markdown_editor
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),  # ckeditor
    url(r'^', include('blog.apps.comments.urls')),  # 评论
]

if settings.DEBUG:
    # 指定静态文件上传的目录(images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 自定义403/404/500页面
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error
