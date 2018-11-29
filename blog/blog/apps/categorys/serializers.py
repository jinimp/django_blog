# -*- coding:utf8 -*-
from categorys.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """查询分类数据序列化器"""

    class Meta:
        model = Category
        fields = '__all__'


class NavDropdownSerializer(serializers.ModelSerializer):
#     """
#     导航栏下拉标签信息序列化器
#     """
#     # 想法: 应该查询分类下的标签,可不可以有视图中新加一个属性,查询出分类对应的标签,然后
#     # 在序列化器中指定该属性为只读,最终返回:
#     # {
#     # R: {'爬虫', '可视化'},
#     # Python: {'爬虫', '可视化'},
#     # ...
#     #  }
#     class Meta:
#         model = Category
#         fields = ('name')
    pass
