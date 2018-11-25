# -*- coding:utf8 -*-

from haystack import indexes
from .models import Article


# 在article应用中新建search_indexes.py文件，用于存放索引类
# 注意:
# 1.在哪个应用下使用搜索功能就在哪个应用下建立该文件
# 2.该文件的文件名固定为search_indexes
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Article索引数据模型类:
    1.在ArticleIndex建立的字段，都可以借助haystack由elasticsearch搜索引擎查询。

    2.其中text字段我们声明为document=True，表名该字段是主要进行关键字查询的字段，
    该字段的索引值可以由多个数据库模型类字段组成，具体由哪些模型类字段组成，我们用use_template=True表示后续通过模板来指明。

    3.在REST framework中，索引类的字段会作为查询结果返回数据的来源。
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return Article

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_delete=False)

