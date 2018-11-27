# -*- coding:utf8 -*-

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from math import ceil


class StandardResultsSetPagination(PageNumberPagination):
    """
    分页paginate用于展示文章列表
    """

    # page_query_param参数(值可随意定义):
    # 1.定义的值会自动往url中查询字符串后面拼接&page=
    # 2.获取url查询字符串中传来的page
    page_query_param = 'page'

    # page_size_query_param参数(值可随意定义):
    # 1.定义的值会自动往url中查询字符串后面拼接&size=
    # 2.获取url查询字符串中传来的size
    page_size_query_param = 'size'

    # 默认每页显示多少条
    # page_size_query_param参数定义的变量可以改变每页显示条数
    page_size = 3

    # 最大支持的每页显示的数据条数
    # 虽然page_size_query_param参数定义的变量可以改变每页显示条数
    # 但是max_page_size可以控制最多每页显示的条数
    max_page_size = 3

    # 由于标准的返回结果中没有分页后的总页数,因此要重写返回的方法,添加上总页数
    def get_paginated_response(self, data):
        # --- 计算总页数 --- #

        # 获取当前每页显示多少条文章
        # 虽然默认是指定显示3条,但是用户可以更改size参数, 因此要动态获取当前显示多少条记录
        per_page_count = self.page.paginator.per_page

        # 获取一共有多少篇文章
        total_count = self.page.paginator.count

        # 计算一共有多少页(向上取整)
        total_page = ceil(total_count/per_page_count)

        # --- 获取当前页码 --- #
        current_page = int(self.request.query_params.get('page', 1))
        # --- 获取当前每页显示多少条 --- #
        size = int(self.request.query_params.get('size', self.page_size))

        # --- 返回结果 --- #
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            # 总记录数(即一共有多少篇文章)
            'total_count': total_count,
            # 当前页数
            'current_page': current_page,
            # 总页数(即一共有多少页)
            'total_page': total_page,
            # 每页显示多少条
            'size': size,
            'results': data
        })

