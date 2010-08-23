# Create your views here.
from django.views.generic.list_detail import object_detail
from annoying.decorators import render_to
from tagging.models import Tag, TaggedItem
from FluxHodgeBlodge.apps.flux.blog.models import Blog

def list_tags (request):
    qs = Tag.objects.all()
    return object_detail(
        request, 
        queryset=qs, 
        template_name='tags/detail.html'
    )
    
# Create your views here.
@render_to("blog/tags.html")
def tags(request):
    return 

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

@render_to("blog/with_tag.html")
def with_tag(request, tag, object_id=None, page=1):
    query_tag = Tag.objects.get(name=tag)
    entries = TaggedItem.objects.get_by_model(Blog, query_tag)
    entries = entries.order_by('-create_date')
    return dict(tag=tag, entries=entries)
