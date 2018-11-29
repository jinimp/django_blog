from django.contrib import admin
from . import models

# --------------------------------------------------------------- #
# ------------------------- 注册文章评论类 ------------------------- #
# --------------------------------------------------------------- #
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    # ------ 详情页的显示 ------ #

    # 在后台文章详情里面显示日期和时间(因为这两个字段很特殊)
    fields = ('user', 'article', 'content', 'parent')

    # 在文章列表页面显示的字段, 不是详情里面的字段
    # 将show_tags函指定到列表中即可显示多对多字段的结果!!
    list_display = ['id',  'user', 'article', 'content', 'parent', 'push_time']

    # 每页显示10条记录
    list_per_page = 10

    # 按最新创建的时间排序. ordering设置默认排序字段，负号表示降序排序
    ordering = ('-push_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('article', 'content')

    # 搜索栏
    search_fields = ['article']

    # 过滤器
    list_filter = ['push_time']
