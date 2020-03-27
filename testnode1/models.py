from django.db import models
# 设计和表对应的类,必须继承自models的Model类，才被认为是model类
# Create your models here.

# 图书类
class BookInfo(models.Model):
    """图书类
    定义类属性
    """
    # CharField，说明是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # DataField是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        """改写其返回的格式，后台admin中会显示表的内容，但是以默认__str__返回的是类对象的格式，手动修改此方法即可"""
        # 返回书名，在后台就能正常看出
        return self.btitle


# 英雄人物类
class HeroInfo(models.Model):
    """和图书类存在多对一关系"""
    hname = models.CharField(max_length=20)
    # BooleanField为布尔类型，default指定默认值，False代表男
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    # 建立和图书类的关系,外键
    # django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname