from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from events.forms import EventCreateForm
from events.models import Event


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

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/event-edit.html'


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event-delete.html'
    success_url = reverse_lazy('events:event-list')