# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from FluxHodgeBlodge.blog.models import Blog, Category

def index(request):
    return render_to_response('index.html',{
        'categories' : Category.objects.all(),
        'posts': Blog.objects.all()[:5],
    })

def view_post(request, slug):
    return render_to_response('view_post.html',{
        'post': get_object_or_404(Blog, slug=slug),
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html',{
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5],
    })

def v_addvideo (request, submissionid):
    manipulator = VideoSubmission.AddManipulator()
    form = FormWrapper(manipulator, {}, {})
    params = {'userAccount':request.user, 'form': form,}
    c = Context (request, params)
    t = loader.get_template('video/addvideo.html')
    sub = Submission.objects.get(pk=submissionid)
    params['submission'] = sub
    return HttpResponse(t.response(c))


