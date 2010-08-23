from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include ('FluxHodgeBlodge.blog.urls')),
    (r'^jobs/', include('FluxHodgeBlodge.jobs.urls')),
    (r'^tumblelog/', include ('FluxHodgeBlodge.tumblelog.urls')),
)

if settings.DEBUG:
    urlpatterns +=patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )