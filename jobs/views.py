#from django.http import HttpResponse
#from django.template import Context, loader
from annoying.decorators import render_to
from jobs.models import Job

# Create your views here.
@render_to('job_list.html')
def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    return {'object_list': object_list}

@render_to('job_detail.html')
def detail(request, job_id):
    job = get_object_or_404 (Job, pk=job_id)
    return {'job': job}