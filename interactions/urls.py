from django.urls import path

from interactions.views import CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'interactions'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]