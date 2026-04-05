from django.urls import path

from interactions.views import CommentCreateView, CommentUpdateView, CommentDeleteView, CommentListView, \
    CommentDetailView

app_name = 'interactions'

urlpatterns = [
    path('', CommentListView.as_view(), name='comment-list'),
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('event/<int:event_id>/', CommentListView.as_view(), name='event-comments'),
    path('group/<int:group_id>/', CommentListView.as_view(), name='group-comments'),
]