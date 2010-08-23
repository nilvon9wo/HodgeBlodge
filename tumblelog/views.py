# Create your views here.
from annoying.decorators import render_to
from FluxHodgeBlodge.tumblelog.models import TumbleItem

@render_to ('tumblelog/list.html')
def tumbler(request):
    return { 'object_list' : TumbleItem.objects.all().order_by('-pub_date') }
