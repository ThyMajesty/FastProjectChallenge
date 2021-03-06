from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from converter.api import v1_api
from converter import views
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
	url(r'^$', views.index),
	
	url(r'^vk_like/$', views.vk_like),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^chain/(?P<src_id>\d+)/(?P<trg_id>\d+)/$', views.chain),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
