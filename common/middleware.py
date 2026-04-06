import time

from django.shortcuts import render
from django.utils.timezone import now

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f"Request took {duration:.2f}s")
        return response

class LastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user.last_login = now()
            request.user.save(update_fields=['last_login'])

        return self.get_response(request)


class ForceCustomErrorPagesMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)

            if response.status_code == 403:
                return render(request, "403.html", status=403)

            elif response.status_code == 404:
                return render(request, "404.html", status=404)

            elif response.status_code == 500:
                return render(request, "500.html", status=500)

            return response

        except Exception:
            return render(request, "generic_error.html", status=500)