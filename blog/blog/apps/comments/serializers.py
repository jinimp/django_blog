# -*- coding:utf8 -*-
from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers
from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField
from articles.models import Article
from articles.search_indexes import ArticleIndex
from categorys.serializers import CategorySerializer


class ArticleCommentSerializer(serializers.ModelSerializer):
    """查询评论序列化器"""

    # PrimaryKeyRelatedField(默认返回外键的id), StringRelatedField(__str__)
    # 使用StringRelatedField字段查询出外键的__str__方法的值
    # 使用序列化器则可以返回对象的全部属性
    # category = StringRelatedField(read_only=True)
    # comment_count = serializers.IntegerField(read_only=True)
    # # 格式化时间格式！
    # create_time = serializers.DateTimeField(format='%Y-%m-%d')
    #
    # class Meta:
    #     model = Article
    #     fields = ('id', 'title', 'abstract', 'click', 'article_image',
    #               'create_time', 'category', 'comment_count')
    pass
