from django.urls import path

app_name = 'common'

urlpatterns = [
    path('', views.home, name='home'),
]