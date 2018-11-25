from QQLoginTool.QQtool import OAuthQQ
from django.conf import settings
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def login_template(request):
    """
    返回登录模板页
    :param request:
    :return:
    """
    return render(request, 'login.html')


def oauth_callback(request):
    """
    返回登录模板页
    :param request:
    :return:
    """
    return render(request, 'oauth_callback.html')


def page_not_found(request, **kwargs):
    """
    返回404页面模板
    :param request:
    :return:
    """
    return render(request, '404.html')


class QQAuthURLView(APIView):
    """提供QQ登录页面网址
    https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=xxx&redirect_uri=xxx&state=xxx
    """

    def get(self, request):
        # next表示从哪个页面进入到的登录页面，将来登录成功后，就自动回到那个页面
        state = request.query_params.get('state', None)

        if state is None:
            state = '/'

        # 初始化生成qq对象
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID,
                        client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI,
                        state=state)

        # 获取跳转连接
        qq_login_url = oauth.get_qq_url()

        # 返回跳转连接给前端
        return Response({'qq_login_url': qq_login_url})


class QQAuthUserView(APIView):

    def get(self, request):
        """获取用户登录成功之后的code, 然后使用这个code值向qq服务器请求用户的openid值"""

        # 登录成功后,　在url后面会有该用户的code值: http://www.linjinquan.com/qqlogin?code=A3A256C8E541AE32AB591976CF1D170A&state=%2F
        # 提取code请求参数
        code = request.query_params.get('code')
        if not code:
            return Response({'message': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)

        # 创建工具对象
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID,
                        client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI)

        try:
            # 使用code向QQ服务器请求access_token
            access_token = oauth.get_access_token(code)
            # 使用access_token向QQ服务器请求openid
            openid = oauth.get_open_id(access_token)
        except Exception:
            return Response({'message': '获取用户信息失败'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        if openid:
            return Response({'message': '200'})
