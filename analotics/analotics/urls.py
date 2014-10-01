from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import parking.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analotics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^lots/$', parking.views.lots, name='lots'),
    url(r'^licenses/$', parking.views.licenses, name='licenses'),
    url(r'^lots/checkin/$', parking.views.checkin, name='checkin'),
    url(r'^admin/', include(admin.site.urls)),
)
