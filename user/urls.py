from django.urls import path
from .views import *
urlpatterns = [
    path("",reg), #blog/urls.py中已经匹配了users/ 多级路径 这里直接填“ ”
    path("login",log),
    path("logout",log_o)
]