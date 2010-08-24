from django import http

class RestView(object):
    methods = ('GET', 'HEAD')
    
    @classmethod
    def dispatch(cls,request, *args, **kwargs):
        resource = cls()
        if request.method.lower() not in (method.lower() for method in resource.methods):
            return http.HttpResponseNotAllowed(resource.methods)
        try:
            method = getattr(resource, request.method.lower())
        except AttributeError:
            raise Exception("View method `%s` does not exist." % request.method.lower())
        if not callable(method):
            raise Exception("View method `%s` is not callable." % request.method.lower())
        return method(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return http.HttpResponse()
    
    def head(self, request, *args, **kwargs):
        response = self.get(request, *args, **kwargs)
        response.content = ''
        return response
    
def add_accessor_methods(self, *args, **kwargs):
    for size in PhotoSizeCache().sizes.keys():
        setattr(self, 'get_%s_size' % size, curry(self.get_SIZE_size, size=size))
        setattr(self, 'get_%s_photosize' % size, curry(self.get_SIZE_photosize, size=size))
        setattr(self, 'get_%s_url' % size, curry(self.get_SIZE_url, size=size))
        setattr(self, 'get_%s_filename' % size, curry(self.get_SIZE_filename, size=size))
                    