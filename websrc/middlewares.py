import requests
from django.shortcuts import render


class HandleExceptionMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # do something ...
        try:
            raise exception
        except (
                requests.HTTPError,
                requests.ConnectionError,
                requests.Timeout,
        ) as e:
            exc_name = e.__class__.__name__
            return render(request, 'error.html', {'exception': e, 'exc_name': exc_name})
