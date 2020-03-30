from django.contrib import admin
from .models import BookInfo,HeroInfo
# 后台管理相关文件
# Register your models here.


# 自定义模型管理类，就是自定义某个类展示的效果，展示哪些列
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'hname', 'hgender', 'hcomment']


# 注册模型类
# 同一个类的注册只能写一次，多次会报错
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
