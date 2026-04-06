from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from events.tasks import send_event_reminder_async
from interactions.forms import CommentForm
from interactions.models import Comment

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'interactions/comment-create.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['group'] = self.request.GET.get('group')
        initial['event'] = self.request.GET.get('event')
        return initial

    def form_valid(self, form):
        print("GET:", self.request.GET)

        form.instance.user = self.request.user

        group_id = self.request.GET.get('group')
        event_id = self.request.GET.get('event')

        print("GROUP:", group_id)
        print("EVENT:", event_id)

        if not group_id and not event_id:
            form.add_error(None, "Comment must belong to a group or event.")
            return self.form_invalid(form)

        if group_id:
            form.instance.group_id = group_id

        if event_id:
            form.instance.event_id = event_id

        response = super().form_valid(form)

        messages.success(self.request, "Comment posted successfully!")
        return response

    def get_success_url(self):
        if self.object.group:
            return self.object.group.get_absolute_url()
        if self.object.event:
            return self.object.event.get_absolute_url()

        return reverse_lazy('common:home')
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'interactions/comment-edit.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Comment updated successfully!")
        return response


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'interactions/comment-delete.html'
    success_url = reverse_lazy('common:home')

    def delete(self, request, *args, **kwargs):
        messages.warning(request, "Comment deleted!")
        return super().delete(request, *args, **kwargs)

class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'interactions/comment-detail.html'

class CommentListView(ListView):
    model = Comment
    template_name = 'interactions/comment-list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        group_id = self.kwargs.get('group_id')

        if event_id:
            return Comment.objects.filter(event_id=event_id)

        if group_id:
            return Comment.objects.filter(group_id=group_id)

        return Comment.objects.all()