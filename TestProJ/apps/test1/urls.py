# apps/test1/urls.py
from django.urls import path
from . import views  # 引入 views.py

urlpatterns = [
    path('', views.index, name='index'),  # 默认首页
    # path('about/', views.about, name='about'),  # 一个额外的页面
]
