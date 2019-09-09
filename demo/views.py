from django.http import HttpResponse
from django.template import Template,Context
def gethtml(request):
    html = """
    <html>
        <head>
        </head>
        <body>
        <h1>图片</h1>
        <a href = "www.baidu.com">
        <img src="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1567996377&di=3878f6fe00da9ad7cd7fcda4a72a73f7&src=http://hbimg.b0.upaiyun.com/28ea2e5cf17173f84ef74064e95627cc3ba75fe627e71-hKNgS4_fw658" title="图" alt="空">
        <p>{{content}}</p>
        </a>
        </body>
    </html>
    """
    # 构建模板结构
    tempalte_obj = Template(html)
    # 创建渲染模板
    params = dict(name='Q',content="风景")
    content_obj = Context(params)
    # 进行数据渲染
    result = tempalte_obj.render(content_obj)
    #返回结果
    #return HttpResponse(html)
    return HttpResponse(result)


from django.shortcuts import render
def indextmp(request):
    name = "藏獒"
    return render(request,'index.html',{"name":name})

from django.shortcuts import render_to_response
def abc (request):
    name = "hello"
    return render_to_response("abc.html",{"name":name})

from django.template.loader import get_template
def abc(request):
    template = get_template('abc.html')
    name = "hello"
    result = template.render({'name':name})
    return HttpResponse(result)