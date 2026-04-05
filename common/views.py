from django.views import View
from django.shortcuts import render


class HomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'common/home-authenticated.html')

        return render(request, 'common/home-anonymous.html')