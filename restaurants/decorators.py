from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def check_user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        if request.session.has_key('token'):
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
#           raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
