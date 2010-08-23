from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include ('FluxHodgeBlodge.apps.flux.blog.urls')),
    (r'^jobs/', include('FluxHodgeBlodge.apps.flux.jobs.urls')),
    (r'^tumblelog/', include ('FluxHodgeBlodge.apps.flux.tumblelog.urls')),
)

urlpatterns += patterns('django.contrib.auth',
    (r'^accounts/login/$', 'views.login', {'template_name':'admin/login.html'}),
    (r'^accounts/login/$', 'views.logout'),
)

if settings.DEBUG:
    urlpatterns +=patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )