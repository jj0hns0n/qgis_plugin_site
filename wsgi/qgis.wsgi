import site, os
import site
site.addsitedir('/home/qgis/.virtualenvs/qgis/lib/python2.7/site-packages')
site.addsitedir('/home/qgis/qgis_plugin_site')

os.environ['DJANGO_SETTINGS_MODULE'] = 'qgis_plugin_site.settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
