from django.db import models


class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=20, verbose_name='标签名称')

    class Meta:
        db_table = 'tb_tag'  # 自定义数据库表的名称
        verbose_name = '标签'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CategoryTag(models.Model):
    """分类标签表"""
    category = models.ForeignKey('categorys.Category', verbose_name='分类')
    tag = models.ForeignKey('tags.Tag', verbose_name='标签')

    class Meta:
        db_table = 'tb_category_tag'  # 自定义数据库表的名称
        verbose_name = '分类标签'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return '分类<%s>下的标签有: %s' % (self.category, self.tag)
