def my_context(request):
    try:
        return dict(my_user=MyUser.objects.get(user=request.user))
    except ObjectNotFound:
        return dict(my_user='')
    