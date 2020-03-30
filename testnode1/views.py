from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
# 1.定义视图函数，定义request，是HttpRequest的对象
# 2. 进行url配置，建立Url地址和视图的对应关系
# http://127.0.0.1/index
def index(request):
    # 进行处理，和M或者和T交互
    # 返回一个HttpResponse对象
    # return HttpResponse('老铁，没毛病！')

    # # 使用模板文件
    # # 1.加载模板文件,返回模板对象
    # temp = loader.get_template('testnode1/index.html')
    # # 2.定义模板上下文，给模板传递数据,request是参数，{}是给模板中传递参数的键值对
    # context = RequestContext(request, {})
    # context.push(locals())
    # # 3.模板渲染：产生标准的HTML
    # res_html = temp.render(context=locals(), request=request)
    # # 4.返回给浏览器
    # return HttpResponse(res_html)
    # 如果每个函数都写加载写入渲染，较为复杂，使用render()简单
    # 先写传入的参数
    context = {'list': range(10)}
    # 渲染返回
    return render(request, 'testnode1/index.html', context)


def index2(request):
    return HttpResponse('<h1>Hello Django</h2>')