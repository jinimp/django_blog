"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 导包路径中添加apps目录
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# ------------------------------ django开发配置参考 ------------------------------ #
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# ------------------------------ 配置秘钥 ------------------------------ #
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pg=x^84dz-f3)$h@=j9wdiow12!*qg*m6#nig2l45n^gcf=7j9'


# ------------------------------ 配置debug ------------------------------ #
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# ------------------------------ 配置允许哪些主机访问后台 ------------------------------ #
ALLOWED_HOSTS = ['*', '127.0.0.1', 'localhost', 'www.linjinquan.com']


# ------------------------------ 配置应用 ------------------------------ #
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 注册第三方应用
    'rest_framework',  # drf框架
    'corsheaders',   # 跨域
    'mdeditor',  # markdown_editor
    # 'ckeditor',  # 富文本编辑器
    # 'ckeditor_uploader',  # 富文本编辑器上传图片模块

    # xmadmin后台管理模块
    # 官方文档：https://xadmin.readthedocs.io/en/latest/quickstart.html#id1

    'haystack',  # haystack是连接elaticsearch搜索引擎服务器的客户端

    # 注册自己创建的应用　
    'users.apps.UsersConfig',  # 用户
    'articles.apps.ArticlesConfig',  # 文章
    'categorys.apps.CategorysConfig',  # 分类
    'tags.apps.TagsConfig',  # 标签
    'comments.apps.CommentsConfig',  # 评论
]


# ------------------------------ 配置中间件 ------------------------------ #
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 跨域

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------ 配置根路由 ------------------------------ #
ROOT_URLCONF = 'blog.urls'


# ------------------------------ 配置模板 ------------------------------ #
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ------------------------------ 配置wsgi ------------------------------ #
WSGI_APPLICATION = 'blog.wsgi.application'


# ------------------------------ 配置mysql数据库 ------------------------------ #
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'HOST': '127.0.0.1',  # 数据库主机
        'HOST': '120.79.166.160',  # 远程数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql_pw_3',  # 数据库用户密码
        'NAME': 'myblog'  # 数据库名字
    }
}


# ------------------------------ 配置redis ------------------------------ #
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",  # 选择0号库存储
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # 选择1号库存储
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# ------------------------------ 密码验证 ------------------------------ #
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ------------------------------ 配置时区/语言 ------------------------------ #
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 设置语言为中文

TIME_ZONE = 'Asia/Shanghai'  # 时区为上海

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ------------------------------ 设置静态文件目录 ------------------------------ #

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 访问的静态文件的时候使用的前缀,而不是静态文件存放的目录的名字(即访问时以/static/访问, 但是存储在/static_files/)
STATIC_URL = '/static/'
# 静态文件存放的位置
STATIC_ROOT = [os.path.join(BASE_DIR, 'static_files')]

# ------------------------------ 配置日志 ------------------------------ #
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/blog.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}


# ------------------------------ 跨域添加白名单 ------------------------------ #
CORS_ORIGIN_WHITELIST = (
    'www.linjinquan.com:8000'
)
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie操作
CORS_ORIGIN_ALLOW_ALL = True  # 支持跨域！！！！！

# ------------------------------ 指定自定义的用户模型类 ------------------------------ #
# 因为django有自带了一个user模型类, 该模型类已经配置好了很多的功能：如, 密码验证功能等
AUTH_USER_MODEL = 'users.User'


# ------------------------------ DRF相关配置 ------------------------------ #
REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'blog.utils.exception.my_exception_handler',
}


# ------------------------------ QQ登录参数 ------------------------------ #
# 自己的应用app_id和app_key
QQ_CLIENT_ID = '101512688'  # appid
QQ_CLIENT_SECRET = '35a2d4c2345f22ce8360b4c7d2ad6575'   # appkey
QQ_REDIRECT_URI = 'http://www.linjinquan.com:8000/qqlogin'  # 登录成功后的回调网址


# ------------------------------ 发送邮件参数 ------------------------------ #
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'linjinquan14@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'meiduo123'
# 收件人看到的发件人
EMAIL_FROM = '博客验证<linjinquan14@163.com>'

# celery运行命令：celery -A celery_tasks.main worker --loglevel=info


# ------------------------------ 富文本编辑器ckeditor配置 ------------------------------ #
# CKEDITOR_CONFIGS = {
#     # 自定义样式1
#     'default': {
#         'toolbar': 'full',  # 工具条功能,使用全部的功能
#         'height': 300,  # 编辑器高度
#         'skin': 'moono',  # 皮肤
#         # codesnippet：可以插入代码高亮; uploadimage：可以复制图片,然后直接粘贴
#         'extraPlugins': ','.join(['codesnippet', 'uploadimage']),  # 插件
#     },
# }
#
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_IMAGE_BACKEND = 'pillow'

# ------------------------------ markdown_editor 配置 ------------------------------ #
# editor.md官方帮助文档（全）：http://pandao.github.io/editor.md/

MDEDITOR_CONFIGS = {
    # 字典一定要有一个键,默认为'default'!
    'default': {
        'width': '90% ',  # Custom edit box width
        'heigth': 500,  # Custom edit box height
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h4", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table",
                    "datetime","emoji", "html-entities", "pagebreak", "goto-line", "clear", "search", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
        'image_floder': 'editor',  # image save the folder name
        'theme': 'dark',  # edit box theme, dark / default
        'preview_theme': 'default',  # Preview area theme, dark / default
        'editor_theme': 'pastel-on-dark',  # edit area theme, pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement
        'emoji': True,  # whether to open the expression function
        'tex': True,  # 支持tex数学公式
        'flow_chart': True,  # 支持FlowChart流程图
        'sequence': True,  # 支持时序图/序列图
        # 'htmlDecode': True,  # 不知道如何开启html标签识别和解析,开启了也识别不了！
    }
}

# 后台上传的图片存储的目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# MEDIA_URL的作用是???
MEDIA_URL = '/media/'


# ------------------------------ Haystack 配置 ------------------------------ #
# 配置haystack这个客户端使用的搜索引擎后端是Elasticsearch
# (如果部署在docker中,需要先在docker中开启Elasticsearch服务)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.56.101:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'myblog',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
# 注意：
# HAYSTACK_SIGNAL_PROCESSOR 的配置保证了在Django运行起来后，有新的数据产生时，
# haystack仍然可以让Elasticsearch实时生成新数据的索引
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 开发环境下:
# 1.在docker中开启elasticsearch容器服务: docker start elasticsearch
    # 1.1检查是否能连接elasticsearch: curl -X GET http://192.168.136.132:9200/_cat/indices
    # 1.2如果连接不上,要删除容器,重新创建容器
# 2.每次启动都要先在终端执行: python manage.py rebuild_index


# ------------------- login_required自定义重定向到登录页面 --------------------- #
LOGIN_URL = '/oauth/login/'
