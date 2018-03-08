=====
DJANGO-RESTRICTMETHODORIGIN
=====

DJANGO-RESTRICTMETHODORIGIN is a simple Django app to bind origins with http methods.
So that its possible to allow ony speicific origins to make speicific http requests like POST, GET, PUT etc. 


Quick start
-----------

1. Add "restrictmethodorigin" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'restrictmethodorigin',
    ]

2. Add "OriginRestrictor" to your MIDDLEWARE like this:
    MIDDLEWARE = [
        ...
        'restrictmethodorigin.base.OriginRestrictor'
    ]

3. In settings.py create a dictionary METHOD_ORIGIN like this:
    METHOD_ORIGIN = { 'POST': ['127.0.0.1'],
                       'PUT': ['127.0.0.1','127.0.0.2'] }

