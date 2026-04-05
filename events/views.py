from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from events.forms import EventCreateForm
from events.models import Event, EventParticipation
from events.tasks import send_event_reminder_async, notify_participants


class EventListView(ListView):
    model = Event
    template_name = 'events/event-list.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event-detail.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/event-create.html'

    # def form_valid(self, form):
    #     form.instance.organizer = self.request.user
    #     return super().form_valid(form)

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        response = super().form_valid(form)

        send_event_reminder_async(
            self.request.user.email,
            form.instance.title
        )
        return response



class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/event-edit.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        notify_participants(self.object)

        return response

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event-delete.html'
    success_url = reverse_lazy('events:event-list')

@login_required
def event_join(request, pk):
    event = get_object_or_404(Event, pk=pk)
    participation, created = EventParticipation.objects.get_or_create(
        user=request.user, event=event, defaults={'status':'going'}
    )
    if created:
        messages.success(request, f'You joined "{event.title}"!')
    else:
        messages.info(request, "You are already participating in this event.")
    return redirect(event.get_absolute_url())

@login_required
def event_leave(request, pk):
    event = get_object_or_404(Event, pk=pk)
    participation = EventParticipation.objects.filter(user=request.user, event=event).first()
    if participation:
        participation.delete()
        messages.warning(request, f'You left "{event.title}"!')
    else:
        messages.info(request, "You are not a participant of this event.")
    return redirect(event.get_absolute_url())