# -*- coding:utf8 -*-
from rest_framework import serializers
from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField
from comments.models import Comment


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


class PostArticleCommentSerializer(serializers.ModelSerializer):
    """新增评论序列化器"""

    # 父评论id只序列化返回
    parent = serializers.IntegerField(read_only=True)
    # 格式化时间格式！(read_only=True:只序列化返回)
    push_time = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Comment
        fields = ('article', 'content', 'parent', 'push_time')

        # 反序列化时对字段进行验证
        extra_kwargs = {
            'content': {
                'min_length': 5,
                'max_length': 255,
                'error_messages': {
                    'min_length': '评论内容最小要输入5个字符！',
                    'max_length': '评论内容最大输入255个字符！',
                }
            },
        }

        def create(self, validated_data):
            """
            创建评论
            """
            comment = Comment.objects.create(
                user=validated_data.get('user'),
                article=validated_data.get('article'),
                content=validated_data.get('content'),
            )
            return comment

