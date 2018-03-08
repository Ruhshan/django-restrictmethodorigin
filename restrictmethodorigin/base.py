from django.conf import settings
from django.http import HttpResponseForbidden

target_methods = settings.METHOD_ORIGIN.keys()

http_methods = ['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'POST', 'PUT']

def OriginRestrictor(get_response):
    def middleware(request):
        forbid = False
        for method in http_methods:
            if request.method==method and method in target_methods:
                allowed_origin = settings.METHOD_ORIGIN[method]
                request_origin = request.META['REMOTE_ADDR']

                if request_origin not in allowed_origin:
                    forbid=True
                    break
        if forbid==True:
            return HttpResponseForbidden()
        
        response = get_response(request)
        return response
    return middleware