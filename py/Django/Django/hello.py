from django.http import HttpResponse
from django.shortcuts import render


def sayHello(request):
    return HttpResponse("Hello world ! ")

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!!!'
    return render(request, 'hello.html', context)

def login(request):
    if request.method == "GET":
        return HttpResponse("GET 方法")
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "xuwujing" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法1")


print("hello")