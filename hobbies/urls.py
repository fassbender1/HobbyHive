from django.urls import path

app_name = 'hobbies'

urlpatterns = [
    path('', HobbyListView.as_view(), name='hobby-list'),
]