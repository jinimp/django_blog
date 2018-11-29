from django.db import models


# -------------------------------------------------------------------------- #
# ------------------------------ 多对多关系表 -------------------------------- #
# -------------------------------------------------------------------------- #

class Comment(models.Model):
    """评论表"""
    user = models.ForeignKey('users.User', verbose_name='用户')
    article = models.ForeignKey('articles.Article', verbose_name='文章')
    content = models.CharField(max_length=255, verbose_name='评论内容')
    # 关联父评论的id, 数据库可以为空, 后台admin也可以为空
    parent = models.ForeignKey(to='self', null=True, blank=True, verbose_name='父评论id')
    push_time = models.DateTimeField(auto_now_add=True, verbose_name="评论发表的时间")

    class Meta:
        db_table = 'tb_comment'  # 自定义数据库表的名称
        verbose_name = '评论'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户<%s>对文章<%s>的评论: (%s)' % (self.user, self.article, self.content)

