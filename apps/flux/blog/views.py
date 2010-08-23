# Create your views here.
from django.shortcuts import get_object_or_404
from django.template import Context, loader
from annoying.decorators import render_to
from FluxHodgeBlodge.apps.flux.blog.models import Blog, Category

@render_to('index.html')
def index(request):
    return {
        'categories' : Category.objects.all(),
        'posts': Blog.objects.all()[:5],
    }

@render_to('view_category.html')
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5],
    }

@render_to('view_post.html')
def view_post(request, slug):
    return { 'post': get_object_or_404(Blog, slug=slug), }

def v_addvideo (request, submissionid):
    manipulator = VideoSubmission.AddManipulator()
    form = FormWrapper(manipulator, {}, {})
    params = {'userAccount':request.user, 'form': form,}
    c = Context (request, params)
    t = loader.get_template('video/addvideo.html')
    sub = Submission.objects.get(pk=submissionid)
    params['submission'] = sub
    return HttpResponse(t.response(c))


