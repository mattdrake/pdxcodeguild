from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registration_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'registration_demo.views.home', name='home'),

    # registration urls
    url(r'^register/$', 'registration_demo.views.register'),
    url(r'^success/$', 'registration_demo.views.success'),

    # login urls
    url(r'^login/$', 'registration_demo.views.login'),
)
