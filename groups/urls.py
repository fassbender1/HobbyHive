
from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='group-list'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('create/', GroupCreateView.as_view(), name='group-create'),
    path('<int:pk>/edit/', GroupUpdateView.as_view(), name='group-edit'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('<int:pk>/join/', group_join, name='group-join'),
    path('<int:pk>/leave/', group_leave, name='group-leave'),
]