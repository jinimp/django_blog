from django.db.models import Count, F
from django.shortcuts import render
from drf_haystack.viewsets import HaystackViewSet
from markdown import markdown
from django_filters import FilterSet, CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article, PageViews
from articles.serializers import ArticleDetailSerializer, LastestArticleSerializer, ArticleListSerializer, \
    ArticleIndexSerializer, ArticleClickRankSerializer
from articles.utils import StandardResultsSetPagination


def article_template(request):
    """
    返回文章详情的模板页
    :param request:
    :return:
    """
    return render(request, 'article_detail.html')


def article_list_template(request):
    """
    返回文章列表的模板页
    :param request:
    :return:
    """
    return render(request, 'article_list.html')


def search_template(request):
    """
    返回文章列表的模板页
    :param request:
    :return:
    """
    return render(request, 'search.html')

# ------------------------------------------------------------------- #
# ----------------------- 首页获取最新的前3篇文章 ----------------------- #
# ------------------------------------------------------------------- #

# --- 方法1: --- #
# class LastestArticleView(APIView):
#     """首页获取最新的前3篇文章"""
#
#     def get(self, request, *args, **kwargs):
#         # 查询出最新发表的前3篇文章
#         query_obj = Article.objects.filter(is_delete=False).order_by('-create_time')[:3]
#         # 给对象加上一个评论的条数这个属性(因为是一个对象,因为加上属性之后,在queryset中也有了)
#         for art_obj in query_obj:
#             # 评论数
#             art_obj.comment_count = art_obj.comment_set.count()
#             # 对文章的创建时间进行格式化
#             art_obj.create_time = art_obj.create_time.strftime('%Y-%m-%d')
#
#         # 序列化返回, 因为返回的结果有多条记录, 因此要使用many=True
#         serializer = LastestArticleSerializer(query_obj, many=True)
#         return Response(serializer.data)


# --- 方法2: --- #
class LastestArticleView(ListAPIView):
    """首页获取最新的前3篇文章"""

    # 指定序列化器
    serializer_class = LastestArticleSerializer

    # 重写get_queryset方法,因为ListAPIView继承的GenericAPIView,
    # 而GenericAPIView会调用get_queryset方法返回一个查询集,
    # 而这个默认的查询集默认是返回所有的数据,因此不符合我们的要求,所以要重写
    def get_queryset(self):
        # 查询出最新发表的前3篇文章
        query_obj = Article.objects.filter(is_delete=False).order_by('-create_time')[:3]
        # 给对象加上一个评论的条数这个属性(因为是一个对象,因为加上属性之后,在queryset中也有了)
        for art_obj in query_obj:
            # 评论数
            art_obj.comment_count = art_obj.comment_set.count()

        # 返回查询集结果
        return query_obj


# ----------------------------------------------------------------------- #
# ----------------------- 首页获取文章列表页数据并分页 ----------------------- #
# ----------------------------------------------------------------------- #

# --- 方法1: --- #
# 方法1继承PageNumberPagination并不会在返回结果中包含next/preview等属性,
# 继承其它的Pagination类就有!或者是用方法2也有!
# class ArticleListView(APIView):
#     """获取文章列表页数据"""
#
#     def get(self, request, *args, **kwargs):
#         # ---------------- 1.获取参数 ------------------- #
#         # 获取文章的id
#         cid = self.request.query_params['cid']
#
#         # ---------------- 2.校验参数 ------------------- #
#
#         # ---------------- 3.业务处理 ------------------- #
#         # 3.1.查询数据库
#         # 应该是查询文章的分类id的值下的所有文章(即category_id而不是文章的id！)
#         query_obj = Article.objects.filter(category_id=cid)
#         # 给查询集修改或添加属性(因为是一个对象,因为加上属性之后,在queryset中也有了)
#         for art_obj in query_obj:
#             # 对文章的创建时间进行格式化
#             art_obj.create_time = art_obj.create_time.strftime('%Y-%m-%d')
#
#         # 3.2.创建分页对象
#         pg = StandardResultsSetPagination()
#
#         # 3.2.1获取分页的数据
#         page_roles = pg.paginate_queryset(queryset=query_obj, request=request, view=self)
#
#         # 3.3.序列化
#         # 查询多篇文章, 因此需要指定many=True, 并指定instance
#         serializer = ArticleListSerializer(instance=page_roles, many=True)
#
#         # ---------------- 4.返回结果 ------------------- #
#         return Response(serializer.data)
#

class TitleFilter(FilterSet):
    """搜索类"""

    title = CharFilter(lookup_expr='icontains')  # 模糊查询（包含），并且忽略大小写
    # title = CharFilter(lookup_expr='iexact')  # 精确匹配

    class Meta:
        model = Article
        fields = ['title']


# --- 方法2: --- #
class ArticleListView(ListAPIView):
    """获取文章列表页数据"""
    # 序列化器
    serializer_class = ArticleListSerializer

    # 分页控制
    pagination_class = StandardResultsSetPagination

    # OrderingFilter：指定排序的过滤器,可以按任意字段排序,通过在路由中通过ordering参数控制,如：?ordering=id
    # DjangoFilterBackend对应filter_fields属性，做相等查询
    # SearchFilter对应search_fields，对应模糊查询
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    # 默认指定按哪个字段进行排序
    ordering_fields = ('-create_time',)
    # 指定可以被搜索字段
    filter_class = TitleFilter

    def get_queryset(self):
        # ---------------- 1.获取参数 ------------------- #
        # 获取文章的id
        cid = self.request.query_params['cid']

        # ---------------- 2.校验参数 ------------------- #

        # ---------------- 3.业务处理 ------------------- #
        # 3.1.查询数据库
        # 应该是查询文章的分类id的值下的所有文章(即category_id, 而不是文章的id！)

        # 返回查询集结果
        # 重写get_queryset中的属性是不行的,get_queryset只返回数据集,想要修改里面的
        # 属性值,去序列化器中修改！！！！！
        return Article.objects.filter(category_id=cid, is_delete=False)


# ------------------------------------------------------------------- #
# ----------------------- 首页获取文章详情页数据 ----------------------- #
# ------------------------------------------------------------------- #

class ArticleDetailView(APIView):
    """获取文章详情页数据"""

    # queryset = Article.objects.filter(id=aid)
    def get(self, request, *args, **kwargs):
        # ---------------- 1.获取参数 ------------------- #
        # 获取文章的id
        try:
            aid = self.request.query_params['aid']
        except:
            return Response({'message': '参数不完整'})

        # ---------------- 2.校验参数 ------------------- #

        # ---------------- 3.业务处理 ------------------- #
        # 3.1.查询数据库
        query_obj = Article.objects.get(id=aid)
        # 3.2点击进入文章详情后,文章的浏览次(点击)数+1
        query_obj.click = F('click') + 1
        # 保存到
        query_obj.save()

        # 重新刷新数据库
        query_obj.refresh_from_db()
        # 3.3.给对象加上一个评论的条数这个属性(因为是一个对象,可以为其加上属性,并且在器就可以使用了)
        query_obj.comment_count = query_obj.comment_set.count()

        # # 3.4用户点击进入文章详情后,文章的浏览次数+1
        # # 如果登录了,才能统计,否则不能统计
        # if request.user.id:
        #     # 查询浏览表中,该用户是否已经浏览过此文章
        #     # filter查询出来的结果是QuerySet类型,使用first之后就才变成对象,才能对属性进行操作！
        #     is_view = PageViews.objects.filter(user_id=request.user.id, article_id=aid).first()
        #     # # 如果有则该用户对该文章的浏览次数+1, 否则则新增一条浏览记录
        #     if is_view:
        #         is_view.frequency += 1
        #         is_view.save()
        #     else:
        #         PageViews.objects.create(user_id=request.user.id, article_id=aid, frequency=1)
        #
        #     # 查询文章的浏览次数(每个用户浏览多次同一篇文章,只算一次)
        #     # 先通过filter筛选对应的文章,然后再统计每篇文章被浏览的次数
        #     article_count = PageViews.objects.filter(article_id=aid).aggregate(article_count=Count('article_id'))
        #     # 上面查询出来的结果是一个字典{'article_count': 1},提取出值,然后保存到page_view中
        #     query_obj.page_view = article_count['article_count']
        #     query_obj.save()

        # 3.5.对保存在数据库中文章内容的的markdown语法转换成html代码(使用markdown模块的markdown函数进行转换)
        # 3.5.1.使用过程中发现了一个问题，就是markdown的换行问题，在前端界面换行显示有问题，并没有br标签，这是因为
        # 在markdown语法中两个空格加一个换行才是换行，或者两个换行才是一个换行
        # 解决办法：可使用article.content.replace(“\r\n”, ’ \n’）解决,把换行符替换成两个空格 + 换行符,
        # 这样经过markdown转换后才可以转成前端的br标签
        query_obj.body = markdown(query_obj.body.replace("\r\n", '  \n'),
                                  extensions=[
                                      'markdown.extensions.extra',  # 支持有些扩展可以手动打开
                                      'markdown.extensions.codehilite',  # 代码高亮
                                      'markdown.extensions.tables',  # 表格处理
                                      'markdown.extensions.toc'  # 支持TOC目录
                                  ], safe_mode=True, enable_attributes=False)

        # 3.6.序列化
        # 查询返回一篇文章,即一个结果,因此不需要指定many=True
        serializer = ArticleDetailSerializer(query_obj)

        # ---------------- 4.返回结果 ------------------- #
        return Response(serializer.data)


# ------------------------------------------------------------------- #
# ----------------------- 文章列表页中的搜索功能 ------------------------ #
# ------------------------------------------------------------------- #

# bug:没有解决当用户输入为空时，出现的bug！！！！！！！！！！！！！！！

# class ArticleSearchViewSet(HaystackViewSet):
#     """
#     Article搜索视图集
#     """
#     # 指定在搜索的时候使用哪个模型类
#     index_models = [Article]
#     # 结果返回时指定的序列化器
#     serializer_class = ArticleIndexSerializer
#     # 指定分页类(不指定会报错,因为HaystackViewSet中要调用)
#     pagination_class = StandardResultsSetPagination


class ArticleSearchView(ListAPIView):

    queryset = Article.objects.filter(is_delete=False)
    # 序列化器
    serializer_class = ArticleListSerializer

    # 分页控制
    pagination_class = StandardResultsSetPagination

    # OrderingFilter：指定排序的过滤器,可以按任意字段排序,通过在路由中通过ordering参数控制,如：?ordering=id
    # DjangoFilterBackend对应filter_fields属性，做相等查询
    # SearchFilter对应search_fields，对应模糊查询
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    # 默认指定按哪个字段进行排序
    ordering_fields = ('-create_time',)
    # 指定可以被搜索字段
    filter_class = TitleFilter


# ------------------------------------------------------------------- #
# ------------------------- 文章点击排行功能 -------------------------- #
# ------------------------------------------------------------------- #

class ArticleClickRankView(ListAPIView):
    """获取点击排行前3篇文章"""

    # 指定序列化器
    serializer_class = ArticleClickRankSerializer

    # 重写get_queryset方法,因为ListAPIView继承的GenericAPIView,
    # 而GenericAPIView会调用get_queryset方法返回一个查询集,
    # 而这个默认的查询集默认是返回所有的数据,因此不符合我们的要求,所以要重写
    def get_queryset(self):
        # 查询出点击排行最多的前3篇文章
        return Article.objects.filter(is_delete=False).order_by('-click')[:3]
