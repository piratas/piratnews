#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import index

urlpatterns = patterns(
    '',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	 url(r'^$', 'piratasnews.views.index', name='home'),
   	 url(r'^', include('opps.urls')),

)


urlpatterns += staticfiles_urlpatterns()
