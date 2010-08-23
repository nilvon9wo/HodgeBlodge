from django.conf.urls.defaults import *
from FluxHodgeBlodge.apps.flux.blog.models import Blog, ENTRY_STATUS_PUBLISHED
from tagging.views import tagged_object_list

dateless_dict={
    'queryset': Blog.objects.filter(status=ENTRY_STATUS_PUBLISHED).order_by('-pub_date'),
}

date_dict={
    'queryset': Blog.objects.filter(status=ENTRY_STATUS_PUBLISHED).order_by('-pub_date'),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^date/$', 'archive_index', dict(date_dict, template_name='blog/list.html')),
    (r'^date/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'object_detail',
        dict(date_dict, slug_field='slug', template_name='blog/detail.html')
    ),
    (r'^date/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', 'archive_day',
        dict(date_dict, template_name='blog/list.html')
    ),
    (r'^date/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month',
        dict(date_dict, template_name='blog/list.html')
    ),
    (r'^date/(?P<year>\d{4})/$', 'archive_year',
        dict(date_dict, template_name='blog/list.html')
    ),

)
urlpatterns += patterns('FluxHodgeBlodge.apps.flux.blog.views',
    url (r'^view/(?P<slug>[^\.]+)', 'view_post', name='view_blog_post'),
    url (r'^category/(?P<slug>[^\.]+)', 'view_category', name='view_blog_category'),
)

urlpatterns += patterns('FluxHodgeBlodge.apps.flux.blog.tag_views',
    #(r'^tags/$', 'tags'),
    url(r'tags/$', 'list_tags', name='tags'),
    #(r'^tag/(?P<tag>[-_A-Za-z0-9]+)/$', 'with_tag'),
    (r'tag/(?P<slug>[-_A-Za-z0-9]+)/$', 'tag_detail'),
    (r'tag/(?P<object_id>[-_A-Za-z0-9]+)/page/(?P<page>d+)$', 'with_tag'),
)

urlpatterns += patterns ('django.views.generic.list_detail',
    url(r'^$', 'object_list', dateless_dict, name="blogs"),
    url(r'^(?P<object_id>\d+)/$', 'object_detail', dateless_dict, name="blog"),
)
