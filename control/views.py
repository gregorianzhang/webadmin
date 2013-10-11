# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from control.models import *


def home(request):
    #if request.user.is_authenticated():
    #ip = machine.objects.raw('select * from control_machine')
    iplist = machine.objects.all()
    cmdlist = machine.objects.all()
    #ip = machine.object.values("ip").all
    para = { "iplist":iplist, "title": "home" ,"cmdlist":cmdlist}
#    para = {"title": "hello world", "current_date": "哦哦哦哦饿", "content": "aa bb cc dd ee", "keywords": "django fabric webadmin", "description": "aaa sss dddd"}
#
    #return HttpResponse(ip)

    return render_to_response("index.html", para)
    #return HttpResponse("<html>Hello world</html>")
    #else:
    #    return HttpResponseRedirect("/error")


def error(request):
    #return render_to_response("account_base.html")
    return HttpResponse("<html>Page is error</html>")
