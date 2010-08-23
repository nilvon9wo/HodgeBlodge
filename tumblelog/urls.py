from django.conf.urls.defaults import *
from models import LatestItems

feeds = {
    'tumblelog' : LatestItems
}

urlpatterns = patterns('',
    (r'^$', 'FluxHodgeBlodge.tumblelog.views.tumbler'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {
        'feed_dict' : feeds
    }),
)
