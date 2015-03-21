from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arda_db.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^browser/', include('browser.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
