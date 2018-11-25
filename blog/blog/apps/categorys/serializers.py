# -*- coding:utf8 -*-
from categorys.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """查询分类数据序列化器"""

    class Meta:
        model = Category
        fields = '__all__'
