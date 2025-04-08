from django.shortcuts import render
from django.http import Http404

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, '404.html', status=404)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return render(request, '404.html', status=404)
        return None