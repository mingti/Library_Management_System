from django.urls import path, include, re_path

from account.views import LoginView



urlpatterns = [

    # 用Knox覆盖登录djoser的路由, 同时knox的login需要单独的设置, 所以再独立出来
    path('auth/token/login/', LoginView.as_view(), name='knox-login'),

    path('auth/token/', include('knox.urls'), name='knox'),
    path('auth/', include('djoser.urls')),

    # path('auth/', include('djoser.urls.authtoken')),


]
