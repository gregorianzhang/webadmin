# Create your views here.
<<<<<<< HEAD

from django.http import HttpResponse

def home(request):
    #if request.user.is_authenticated():
        #return render_to_response("account_base.html")
    return HttpResponse("<html>Hello world</html>")
    #else:
    #    return HttpResponseRedirect("/error")


def error(request):
    #return render_to_response("account_base.html")
    return HttpResponse("<html>Page is error</html>")
=======
>>>>>>> origin/master
