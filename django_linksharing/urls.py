from django.conf.urls.defaults import *

urlpatterns = patterns('django_linksharing.views',
    (r'^$', 'user_index'),
    (r'^list/(?P<username>\w+)/$', 'user_links'),
    (r'^link/add/$', 'link_add'),
    (r'^link/(?P<link_id>\d+)/$', 'link_detail'),
    (r'^link/(?P<link_id>\d+)/change/$', 'link_change'),
    (r'^index/$', 'link_index'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^login/$', 'login',
        {'template_name': 'django_linksharing/login.html'}),
    (r'^logout/$', 'logout',
        {'next_page': '/links/',}),
)
