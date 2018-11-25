from django.contrib import admin
from . import models


# --------------------------------------------------------------- #
# -------------------------- 注册文章类 --------------------------- #
# --------------------------------------------------------------- #
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    # ------ 详情页的显示 ------ #

    # 在后台文章详情里面显示日期和时间(因为这两个字段很特殊)
    # 这里多对多指定的是模型类里指定的字段名tags
    # fields = ('title', 'abstract', 'article_image', 'category', 'tags', 'author',
    #           'body', 'create_time', 'update_time', 'page_view', 'is_delete')

    # fieldsets可以对字段分块, 看起来比较整洁, 层次分明
    fieldsets = (
        ("基本信息", {'fields': ['author', 'article_image', 'category', 'tags']}),
        ("文章内容", {'fields': ['title', 'abstract', 'body']}),
        ("其它信息", {'fields': ['create_time', 'update_time', 'page_view', 'is_delete']})
    )

    # ManyToManyField字段时，使用filter_horizontal, 横排选择其中的一个或多个属性
    filter_horizontal = ('tags',)

    # ------ 列表页的显示 ------- #

    # 定义一个函数, 循环查询出多对多标签表中的所有标签名称, 用于在后台admin站点显示！
    def show_tags(self, obj):
        return [i.name for i in obj.tags.all()]

    # 在文章列表页面显示的字段, 不是详情里面的字段
    # 将show_tags函指定到列表中即可显示多对多字段的结果!!
    list_display = ['title', 'create_time', 'update_time', 'author',
                    'category', 'show_tags', 'page_view', 'is_delete']

    # 每页显示10条记录
    list_per_page = 10

    # 按最新创建的时间排序. ordering设置默认排序字段，负号表示降序排序
    ordering = ('-create_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('title', 'category')

    # 搜索栏
    search_fields = ['title']

    # 过滤器
    list_filter = ['category', 'create_time']


# --------------------------------------------------------------- #
# ------------------------- 注册文章评论类 ------------------------- #
# --------------------------------------------------------------- #
admin.site.register(models.Comment)


# --------------------------------------------------------------- #
# ------------------------- 注册文章浏览类 ------------------------- #
# --------------------------------------------------------------- #
admin.site.register(models.PageViews)
