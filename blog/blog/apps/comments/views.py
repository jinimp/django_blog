from rest_framework.generics import ListAPIView
from comments.serializers import ArticleCommentSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

# ------------------------------------------------------------------- #
# ------------------------- 文章评论功能 ------------------------------ #
# ------------------------------------------------------------------- #


# 装饰类：login_required装饰类时还需要一个method_decorator装饰器
@method_decorator(login_required, name='dispatch')
class ArticleCommentView(ListAPIView):
    """获取评论内容"""

    # 指定序列化器
    serializer_class = ArticleCommentSerializer

    # 重写get_queryset方法,因为ListAPIView继承的GenericAPIView,
    # 而GenericAPIView会调用get_queryset方法返回一个查询集,
    # 而这个默认的查询集默认是返回所有的数据,因此不符合我们的要求,所以要重写
    # def get_queryset(self):
    #     # 查询出点击排行最多的前3篇文章
    #     return Article.objects.filter(is_delete=False).order_by('-click')[:3]
    pass