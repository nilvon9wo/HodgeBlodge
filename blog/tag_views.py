# Create your views here.
import django.http as http
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.list_detail import object_detail
from tagging.models import Tag, TaggedItem
from FluxHodgeBlodge.blog.models import Blog

def list_tags (request):
    qs = Tag.objects.all()
    return object_detail(
        request, 
        queryset=qs, 
        template_name='tags/detail.html'
    )
    
# Create your views here.
def tags(request):
    return render_to_response("blog/tags.html")

def tag_detail(request, slug):
    unslug = slug.replace('-',' ')
    tag = Tag.objects.get(name=unslug)
    qs = TaggedItem.objects.get_by_model(Blog,tag)
    return object_detail(
        request, 
        queryset=qs, 
        extra_context={'tag':slug},
        template_name='tags/detail.html'
    )

def with_tag(request, tag, object_id=None, page=1):
    query_tag = Tag.objects.get(name=tag)
    entries = TaggedItem.objects.get_by_model(Blog, query_tag)
    entries = entries.order_by('-create_date')
    return render_to_response("blog/with_tag.html", dict(tag=tag, entries=entries))

def TEST_tags(request):
    return render_to_response('base.html',{})
