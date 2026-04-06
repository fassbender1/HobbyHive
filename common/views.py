from django.views import View
from django.shortcuts import render


class HomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'common/home-authenticated.html')

        return render(request, 'common/home-anonymous.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def custom_403(request, exception):
    return render(request, '403.html', status=403)