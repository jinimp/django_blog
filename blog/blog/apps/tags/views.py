from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article
from articles.utils import StandardResultsSetPagination
from tags.models import CategoryTag, Tag
from tags.serializers import CategoryTagSerializer, ArticleTagSerializer


def tag_template(request):
    """
    返回一个空的标签页模板
    :param request:
    :return:
    """
    return render(request, 'tag.html')


class TagView(APIView):
    """查询分类下的所有标签"""

    def get(self, request, *args, **kwargs):
        # ---------------- 1.获取参数 ------------------- #
        # 获取分类的id
        try:
            # 获取指定分类下的标签
            cid = self.request.query_params['cid']
            # ---------------- 3.业务处理 ------------------- #
            query_ = CategoryTag.objects.filter(category_id=cid)
        except:
            # ---------------- 3.业务处理 ------------------- #
            # 如果没有传入cid值,则查询所有的标签名称
            query_ = CategoryTag.objects.all()

        # ---------------- 4.返回结果 ------------------- #
        # 如果返回查询出是多个结果,需要指定many=True
        serializer = CategoryTagSerializer(query_, many=True)
        return Response(serializer.data)


class ArticleTagView(ListAPIView):
    """查询标签对应的文章"""

    # 序列化器
    serializer_class = ArticleTagSerializer

    # 分页控制
    pagination_class = StandardResultsSetPagination

    # 排序处理
    # 排序的过滤器
    filter_backends = [OrderingFilter]

    # 指定可以根据哪此字段进行排序
    # ordering_fields = ('title', )
    # 指定按哪个字段进行排序
    ordering = ('-create_time',)

    def get_queryset(self):
        # ---------------- 1.获取参数 ------------------- #

        # 获取标签的id
        try:
            # 获取指定的标签
            tid = self.request.query_params['tid']
            # 获取该分类的id
            cid = self.request.query_params['cid']
            # ---------------- 3.业务处理 ------------------- #
            query_obj = Article.objects.filter(tags=tid, category_id=cid)
        except:
            # ---------------- 3.业务处理 ------------------- #
            # 如果没有传入tid值,则查询所有的标签名称对应的文章
            query_obj = Article.objects.all()

        # 给查询集修改或添加属性,通过如下方法是不起作用的,因此不要在视图中修改属性值，
        # 在序列化器中修改即可！！！
        # for art_obj in query_obj:
        #     # 对文章的创建时间进行格式化
        #     art_obj.create_time = art_obj.create_time.strftime('%Y-%m-%d')

        # 返回查询集结果
        return query_obj
