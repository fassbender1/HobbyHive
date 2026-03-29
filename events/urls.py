from django.urls import path

from events.views import EventCreateView, EventDetailView, EventListView, EventUpdateView, EventDeleteView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]