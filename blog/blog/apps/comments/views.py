from rest_framework.generics import ListAPIView, CreateAPIView
from comments.models import Comment
from comments.serializers import ArticleCommentSerializer, PostArticleCommentSerializer
from rest_framework.permissions import IsAuthenticated


# ------------------------------------------------------------------- #
# ------------------------- 文章评论功能 ------------------------------ #
# ------------------------------------------------------------------- #


class ArticleCommentView(ListAPIView):
    """获取评论内容"""

    # 指定序列化器
    serializer_class = ArticleCommentSerializer

    # 重写get_queryset方法,因为ListAPIView继承的GenericAPIView,
    # 而GenericAPIView会调用get_queryset方法返回一个查询集,
    # 而这个默认的查询集默认是返回所有的数据,因此不符合我们的要求,所以要重写
    def get_queryset(self):
        # 查询出点击排行最多的前3篇文章
        return Comment.objects.filter(article=1)


class PostArticleCommentView(CreateAPIView):
    """新增评论内容"""

    # 指定序列化器
    serializer_class = PostArticleCommentSerializer
    # 访问视图必须要求用户已通过认证（即登录之后）
    # permission_classes = [IsAuthenticated]

