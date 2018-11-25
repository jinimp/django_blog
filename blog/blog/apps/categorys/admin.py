from django.contrib import admin
from . import models


# ------------------------------------------------------------ #
# ------------------------- 注册分类类 ------------------------- #
# ------------------------------------------------------------ #
@admin.register(models.Category)
class ArticleAdmin(admin.ModelAdmin):

    # ------ 列表页的显示 ------- #

    # 在文章列表页面显示的字段, 不是详情里面的字段
    # 将show_tags函指定到列表中即可显示多对多字段的结果!!
    list_display = ['id', 'name', 'describe']

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')
