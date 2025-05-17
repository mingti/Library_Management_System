from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication





class LoginView(KnoxLoginView):
    """
    覆盖knox的默认登录视图,因为默认的登录使用以下权限和认证类:
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated,)

    当DEFAULT_AUTHENTICATION_CLASSES只包含TokenAuthentication时,第一次登录不能包含Token,所以导致登录失败
    这里使用BasicAuthentication,第一次登录时则可以正常返回Token

    具体可以参考官方文档:
    https://jazzband.github.io/django-rest-knox/auth/#global-usage-on-all-views

    """
    authentication_classes = [BasicAuthentication]
