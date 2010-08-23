from django.conf.urls.defaults import *
from jobs.models import Job

info_dict = {
    'queryset': Job.objects.all()
}

urlpatterns = patterns('django.views.generic.list_detail',  #'djproject.jobs.views',
    #(r'^$', 'index'),
    (r'^$', 'object_list', info_dict),
    #(r'^(?P<job_id>\d+)/$', 'detail'),
    (r'^(?P<object_id>\d+)/$', 'object_detail', info_dict),
)
