"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 项目的urls文件
urlpatterns = [
    path('admin/', admin.site.urls),# 配置项目
    # 这里的index1是url http://127.0.0.1/index1/index2/中的第一个index
    # path('index1/', include('testnode1.urls')), # 包含新创建应用中的urls文件
    # 正常情况下，不要在项目的urls文件中进行配置url路径
    path('', include('testnode1.urls')),
]
