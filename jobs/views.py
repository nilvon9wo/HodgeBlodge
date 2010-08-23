#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
#from django.template import Context, loader
from jobs.models import Job

# Create your views here.
def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    return render_to_response('job_list.html',
                              {'object_list': object_list})

def detail(request, job_id):
    job = get_object_or_404 (Job, pk=job_id)
    return render_to_response('job_detail.html',
                              {'job': job})