# Create your views here.
from django.shortcuts import render_to_response
from FluxHodgeBlodge.tumblelog.models import TumbleItem

def tumbler(request):
    context = {
        'object_list' : TumbleItem.objects.all().order_by('-pub_date')
    }
    return render_to_response ('tumblelog/list.html', context)
