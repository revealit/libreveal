""" Utility view functions """
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError

def uwsgi_reload(request):
    allowed_ips = getattr(settings, 'INTERNAL_IPS', ('127.0.0.1',),)

    if request.META['REMOTE_ADDR'] in allowed_ips:
        try:
            import uwsgi
            uwsgi.reload()
            return HttpResponse('Reload OK')
        except ImportError:
            return HttpResponseServerError('Failed to import uwsgi')

    return HttpResponseForbidden('Access denied. You are not on the INTERNAL_IPS list')

