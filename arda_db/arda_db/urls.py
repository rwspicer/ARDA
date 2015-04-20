from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin

from browser import views
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'browser.views.home', name='home'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^how_to_use/$', TemplateView.as_view(template_name='how_to_use.html'), name='how_to_use'),
    url(r'^results/$', TemplateView.as_view(template_name='results.html'), name='results'),
    url(r'^events/$', 'browser.views.events', name='events'),
    url(r'^(?P<r_id>\d+)/$', views.detail, name='detail'),
    url(r'^result/$', views.result),
    
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
