# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from control.models import *


from django.core.context_processors import  csrf
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def ipcmd(request):
    data = ""
    if request.method == 'POST':
        for key in request.POST:
            print key
            data = request.POST.getlist(key)
    print data
    if data == "":
        data = "111"

    return HttpResponse(data)


@csrf_protect
def home(request):
    #if request.user.is_authenticated():
    #ip = machine.objects.raw('select * from control_machine')
    iplist = machine.objects.all()
    cmdlist = cmd.objects.all()
    #ip = machine.object.values("ip").all
    para = { "iplist":iplist, "title": "home" ,"cmdlist":cmdlist}
#    para = {"title": "hello world", "current_date": "哦哦哦哦饿", "content": "aa bb cc dd ee", "keywords": "django fabric webadmin", "description": "aaa sss dddd"}
#
    #return HttpResponse(ip)

    return render_to_response("index.html",
                              para,
                              context_instance=RequestContext(request))
    #return HttpResponse("<html>Hello world</html>")
    #else:
    #    return HttpResponseRedirect("/error")


def error(request):
    #return render_to_response("account_base.html")
    return HttpResponse("<html>Page is error</html>")
