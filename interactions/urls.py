from django.urls import path

from interactions.views import CommentCreateView

app_name = 'interactions'

urlpatterns = [
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
]