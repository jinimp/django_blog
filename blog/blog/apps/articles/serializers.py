# -*- coding:utf8 -*-
from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers
from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField
from articles.models import Article
from articles.search_indexes import ArticleIndex
from categorys.serializers import CategorySerializer


class LastestArticleSerializer(serializers.ModelSerializer):
    """查询文章序列化器"""

    # PrimaryKeyRelatedField(默认返回外键的id), StringRelatedField(__str__)
    # 使用StringRelatedField字段查询出外键的__str__方法的值
    # 使用序列化器则可以返回对象的全部属性
    category = StringRelatedField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)
    # 格式化时间格式！
    create_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Article
        fields = ('id', 'title', 'abstract', 'click', 'article_image',
                  'create_time', 'category', 'comment_count')


class ArticleListSerializer(serializers.ModelSerializer):
    """查询列表页序列化器"""
    # 返回文章所属的分类id
    category_id = serializers.IntegerField(read_only=True)
    # PrimaryKeyRelatedField(默认返回外键的id), StringRelatedField(__str__)
    # 使用StringRelatedField字段查询出外键的__str__方法的值
    # 使用序列化器则可以返回对象的全部属性
    author = StringRelatedField(read_only=True)
    # 多对多字段的序列化返回,并显示__str__而不是id！！操作和一对多一样,只是多对多返回多个,要加个many=True!!
    tags = StringRelatedField(read_only=True, many=True)
    # 格式化时间格式！
    create_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'abstract', 'tags',
                  'create_time', 'category_id', 'article_image')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """查询文章详情序列化器"""

    # PrimaryKeyRelatedField(默认返回外键的id), StringRelatedField(__str__)
    # 使用StringRelatedField字段查询出外键的__str__方法的值
    # 使用序列化器则可以返回对象的全部属性　:href="'/article_list/?cid=' + "
    category = CategorySerializer(read_only=True)
    author = StringRelatedField(read_only=True)
    tags = StringRelatedField(many=True, read_only=True)  # 返回一个列表包括多个结果,　用many=True
    comment_count = serializers.IntegerField(read_only=True)
    # 格式化时间格式！
    create_time = serializers.DateTimeField(format='%Y-%m-%d')
    click = StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'create_time', 'title', 'body', 'page_view',
                  'author', 'category', 'tags', 'comment_count', 'click')


class ArticleIndexSerializer(HaystackSerializer):
    """
    Article索引结果数据序列化器
    """
    # 引用ArticleListSerializer序列化器返回的结果
    object = ArticleListSerializer(read_only=True)

    class Meta:
        # 指定搜索类
        index_classes = [ArticleIndex]
        # 返回的字段内容:
        # 1.text为分词后的文本
        # 2.object为类属性中指定的ArticleListSerializer序列化器返回的结果
        fields = ('text', 'object')


class ArticleClickRankSerializer(serializers.ModelSerializer):
    """
    Article点击排行序列化器
    """

    class Meta:
        model = Article
        fields = ('id', 'title', 'click')
