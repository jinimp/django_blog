# from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mdeditor.fields import MDTextField
from blog.utils.models import BaseModel


class Article(BaseModel):
    """文章表"""

    # 普通字段
    title = models.CharField(max_length=50, verbose_name='标题')
    # body = RichTextUploadingField(verbose_name='内容')
    body = MDTextField(verbose_name='内容')
    abstract = models.TextField(verbose_name='摘要', blank=True)
    # 浏览量可通过浏览表计算出来（有用户登录的前提下）
    page_view = models.IntegerField(verbose_name='浏览量', default=0)
    # 文章的点击量（无用户登录的前提下）
    click = models.IntegerField(verbose_name='点击量', default=0)
    # null = True允许数据库中为空, blank = True允许admin后台中为空
    # 后期不应该设置可以为空的,　应该设置一个设置值(即默认的图片)
    article_image = models.ImageField(verbose_name='文章图片', null=True)
    # 外键
    author = models.ForeignKey('users.User', on_delete=models.PROTECT,
                               related_name='author_article', verbose_name='作者')
    category = models.ForeignKey('categorys.Category', on_delete=models.PROTECT,
                                 related_name='category_article', verbose_name='文章所属的分类')
    tags = models.ManyToManyField('tags.Tag', verbose_name='文章所属的标签')
    # 是否逻辑删除
    is_delete = models.BooleanField(verbose_name='是否逻辑删除', default=False)

    class Meta:
        db_table = 'tb_article'  # 自定义数据库表的名称
        verbose_name = '文章'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# -------------------------------------------------------------------------- #
# ------------------------------ 多对多关系表 -------------------------------- #
# -------------------------------------------------------------------------- #

class Comment(models.Model):
    """评论表"""
    user = models.ForeignKey('users.User', verbose_name='用户')
    article = models.ForeignKey('articles.Article', verbose_name='文章')
    content = models.CharField(max_length=50, verbose_name='评论内容')

    class Meta:
        db_table = 'tb_comment'  # 自定义数据库表的名称
        verbose_name = '评论'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户<%s>对文章<%s>的评论: (%s)' % (self.user_id, self.article_id, self.content)


class PageViews(models.Model):
    """用户文章浏览"""
    user = models.ForeignKey('users.User', verbose_name='用户')
    article = models.ForeignKey('articles.Article', verbose_name='文章')
    frequency = models.IntegerField(verbose_name='用户浏览该文章的次数')

    class Meta:
        db_table = 'tb_page_view'  # 自定义数据库表的名称
        verbose_name = '浏览记录'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户<%s>对文章<%s>浏览了: (%s)次' % (self.user_id, self.article_id, self.frequency)
