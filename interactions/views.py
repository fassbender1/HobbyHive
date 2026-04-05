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
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        event_id = self.request.GET.get('event')
        group_id = self.request.GET.get('group')

        if event_id:
            form.instance.event_id = event_id
        elif group_id:
            form.instance.group_id = group_id
        else:
            form.add_error(None, "Comment must belong to a group or event.")
            return self.form_invalid(form)

        response = super().form_valid(form)

        if form.instance.group:
            send_event_reminder_async(
                form.instance.group.owner.email,
                "New comment on your group"
            )
        if form.instance.event:
            send_event_reminder_async(
                form.instance.event.organizer.email,
                "New comment on your event"
            )

        messages.success(self.request, "Comment posted successfully!")
        return response
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