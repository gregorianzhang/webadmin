from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from control.views import *

from control.models import user
admin.site.register(user)

from control.models import user_login_history
admin.site.register(user_login_history)

from control.models import competence
admin.site.register(competence)

from control.models import machine
admin.site.register(machine)

from control.models import cmd
admin.site.register(cmd)

from control.models import cmd_history
admin.site.register(cmd_history)

from control.models import menu
admin.site.register(menu)




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webadmin.views.home', name='home'),
    # url(r'^webadmin/', include('webadmin.foo.urls')),

    #url(r'^/$', home),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'control.views.home', name='home'),
    url(r'^error/$', error),
    url(r'^ipcmd/$', ipcmd),
    url(r'^aaa/$', aaa),


)
