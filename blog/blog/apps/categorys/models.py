from django.db import models


class Category(models.Model):
    """分类表"""
    name = models.CharField(max_length=20, verbose_name='分类名称')
    describe = models.CharField(max_length=100, verbose_name='描述')
    # null = True允许数据库中为空, blank = True允许admin后台中为空
    category_image = models.ImageField(verbose_name='分类图片', null=True, blank=True)

    class Meta:
        db_table = 'tb_category'  # 自定义数据库表的名称
        verbose_name = '分类'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
