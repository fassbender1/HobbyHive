from django.urls import path

from hobbies.views import HobbyListView, HobbyCreateView, HobbyDetailView, HobbyUpdateView, HobbyDeleteView, hobby_join, \
    hobby_leave

app_name = 'hobbies'

urlpatterns = [
    path('', HobbyListView.as_view(), name='hobby-list'),
    path('create/', HobbyCreateView.as_view(), name='hobby-create'),
    path('<int:pk>/', HobbyDetailView.as_view(), name='hobby-detail'),
    path('<int:pk>/edit/', HobbyUpdateView.as_view(), name='hobby-edit'),
    path('<int:pk>/delete/', HobbyDeleteView.as_view(), name='hobby-delete'),
    path('<int:pk>/join/', hobby_join, name='hobby-join'),
    path('<int:pk>/leave/', hobby_leave, name='hobby-leave'),
]