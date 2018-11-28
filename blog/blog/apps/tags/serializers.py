# -*- coding:utf8 -*-
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from articles.models import Article
from categorys.serializers import CategorySerializer
from tags.models import CategoryTag


class CategoryTagSerializer(serializers.ModelSerializer):
    """查询分类下的标签列化器"""

    # PrimaryKeyRelatedField(默认返回外键的id), StringRelatedField(__str__)
    # 使用StringRelatedField字段查询出外键的__str__方法的值
    # 使用序列化器则可以返回对象的全部属性
    category = CategorySerializer(read_only=True)
    tag = StringRelatedField(read_only=True)

    class Meta:
        model = CategoryTag
        # 注意tag_id才是标签的id！！
        fields = ('id', 'category', 'tag', 'tag_id')


class ArticleTagSerializer(serializers.ModelSerializer):
    """查询标签下的文章序列化器"""

    # 返回文章所属的分类id
    category_id = serializers.IntegerField(read_only=True)
    # PrimaryKeyRelatedField(默认返回外键的id), StringRelatedField(__str__)
    # 使用StringRelatedField字段查询出外键的__str__方法的值
    # 使用序列化器则可以返回对象的全部属性
    author = StringRelatedField(read_only=True)
    # 多对多字段的序列化返回,并显示__str__而不是id！！操作和一对多一样,只是多对多返回多个,要加个many=True!!
    tags = StringRelatedField(read_only=True, many=True)
    # 格式化时间格式！
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'abstract', 'tags',
                  'create_time', 'category_id', 'article_image')
