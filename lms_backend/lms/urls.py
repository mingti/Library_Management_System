from django.urls import path, include
from . import views

from rest_framework import routers

from .views import BookViewSet

routers = routers.DefaultRouter()
routers.register('books', BookViewSet)

urlpatterns = [

    path("", include(routers.urls)),

]
