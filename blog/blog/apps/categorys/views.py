from django.shortcuts import render
from rest_framework.generics import ListAPIView
from categorys.models import Category
from categorys.serializers import CategorySerializer


class CategoryView(ListAPIView):
    """首页获取分类数据"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
