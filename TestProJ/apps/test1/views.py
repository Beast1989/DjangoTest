from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')  # 渲染首页模板

def about(request):
    return HttpResponse("This is the About page for Test1.")  # 返回一个简单的响应