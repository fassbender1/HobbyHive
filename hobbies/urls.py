from django.urls import path

from hobbies.views import HobbyListView, HobbyCreateView, HobbyDetailView, HobbyUpdateView, HobbyDeleteView

app_name = 'hobbies'

urlpatterns = [
    path('', HobbyListView.as_view(), name='hobby-list'),
    path('create/', HobbyCreateView.as_view(), name='hobby-create'),
    path('<int:pk>/', HobbyDetailView.as_view(), name='hobby-detail'),
    path('<int:pk>/edit/', HobbyUpdateView.as_view(), name='hobby-edit'),
    path('<int:pk>/delete/', HobbyDeleteView.as_view(), name='hobby-delete'),
]