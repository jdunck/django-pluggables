from django.conf import settings
from django.conf.urls.defaults import url, include, patterns, handler404, handler500
from django.contrib import admin

from complaints.views import Complaints
from sillywalks import views

admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name='index'),
    url('^sillywalks/$', views.index, name='sillywalks_index'),
    url('^sillywalks/create/$', views.edit, name='sillywalks_create'),
    url('^sillywalks/(?P<walk_name>[\w\-_]+)/$', views.view, name='sillywalks_view'),
    url('^sillywalks/(?P<walk_name>[\w\-_]+)/edit/$', views.view, name='sillywalks_edit'),
    url('^sillywalks/(?P<walk_name>[\w\-_]+)/complaints/', include(views.complaints)),
    url('^complaints/', include(Complaints())),
)

urlpatterns += patterns('',
    url('^django-admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))
