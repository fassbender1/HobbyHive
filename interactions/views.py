from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from interactions.forms import CommentForm
from interactions.models import Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = 'common:home'

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm