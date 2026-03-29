from django.urls import path

from api.views import GroupListAPI

app_name = 'api'

urlpatterns = [
    path('groups/', GroupListAPI.as_view()),
]