import os
import sys
sys.path.append('/home/roy/PycharmProjects/webadmin/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'webadmin.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
