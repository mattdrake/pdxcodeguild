from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'in_the_mood_for.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'in_the_mood_for.views.home', name='home'),

    # horror
    url(r'^horror/$', 'in_the_mood_for.views.horror'),

    # sci-fi
    url(r'^sci_fi/$', 'in_the_mood_for.views.sci_fi'),

    # romance/romantic comedy
    url(r'^romance/$', 'in_the_mood_for.views.romance'),

    # action
    url(r'^action/$', 'in_the_mood_for.views.action'),

    # action
    url(r'^comedy/$', 'in_the_mood_for.views.comedy'),

    # fantasy
    url(r'^fantasy/$', 'in_the_mood_for.views.fantasy'),
)