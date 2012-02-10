import os
import sys
now = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0,now)
sys.path.insert(0,os.path.join(now,"../"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'avagata.deploy_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

