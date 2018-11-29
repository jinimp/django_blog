from django.shortcuts import render
from rest_framework.generics import ListAPIView
from categorys.models import Category
from categorys.serializers import CategorySerializer, NavDropdownSerializer


class CategoryView(ListAPIView):
    """首页获取分类数据"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ------------------------------------------------------------------- #
# ------------------------- 导航栏下拉标签功能 -------------------------- #
# ------------------------------------------------------------------- #

class NavDropdownView(ListAPIView):
    """获取导航栏下拉标签所有的信息"""

    # 指定序列化器
    serializer_class = NavDropdownSerializer

    # 重写get_queryset方法,因为ListAPIView继承的GenericAPIView,
    # 而GenericAPIView会调用get_queryset方法返回一个查询集,
    # 而这个默认的查询集默认是返回所有的数据,因此不符合我们的要求,所以要重写
    # def get_queryset(self):
    #     # 查询出点击排行最多的前3篇文章
    #     return Article.objects.filter(is_delete=False).order_by('-click')[:3]
    pass

