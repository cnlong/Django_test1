from django.urls import path
from . import views


# 通过url 函数设置url路由配置项，将页面请求的Url和函数对应起来
urlpatterns = [
    # 这里的index2是url http://127.0.0.1/index1/index2/中的第一个index
    path('index2/', views.index2), # 建立/index和视图index之间的关系
    path('books/', views.show_books), # 显示图书信息
    path('books/<int:bid>/', views.detail), # 显示英雄信息,这里的<int:bid>就对应传入到后面函数的bid参数
    path('', views.index),
]