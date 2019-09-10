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


def tpltest(request):
    name = "zhangsan"
    age = 19
    hobby = ["eat","sing","pingpang","drink"]
    score = {"math":89,"english":90,"chinese":98}

    # return render(request,"tpltest.html",{"name":name,"age":age,"hobby":hobby,"score":score})
    return render(request,"tpltest.html",locals())

def tpltest(request,age):
    print(age)
    print(type(age))
    class Say(object):
        def say(self):
            return "hello"

    name = 'zhangsan'
    age=17
    age = int(age)
    hobby = ["eat","sing","pingpang","drink"]
    score = {"math":89,"english":90,"chinese":98}
    say = Say()
    myjs = """
    <script>
    alert("hello">
    </script>
    """

    return render(request, "tpltest.html", locals())

def test(request):
    return render(request,"statictest.html")

def staticdemo(request):
    params = [
        {"name": "01", "img": "01.jpg", "url": "https:www.sina.com"},
        {"name": "02", "img": "02.jpg", "url": "https:www.baidu.com"},
        {"name": "03", "img": "03.jpg", "url": "https:www.sina.com"},
        {"name": "04", "img": "04.jpg", "url": "https:www.taobao.com"},
        {"name": "05", "img": "05.jpg", "url": "https:www.taobao.com"},
    ]
    return render(request,"staticdemo.html",locals())