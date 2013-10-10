# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    #if request.user.is_authenticated():
    para = {"title": "hello world", "current_date": "哦哦哦哦饿", "content": "aa bb cc dd ee", "keywords": "django fabric webadmin" }
#    para = {"title": "hello world", "current_date": "哦哦哦哦饿", "content": "aa bb cc dd ee", "keywords": "django fabric webadmin", "description": "aaa sss dddd"}

    return render_to_response("index.html", para)
    #return HttpResponse("<html>Hello world</html>")
    #else:
    #    return HttpResponseRedirect("/error")


def error(request):
    #return render_to_response("account_base.html")
    return HttpResponse("<html>Page is error</html>")
