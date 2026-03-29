from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from hobbies.models import Hobby


class HobbyListView(ListView):
    model = Hobby
    template_name = 'hobbies/hobby-list.html'


class HobbyDetailView(DetailView):
    model = Hobby
    template_name = 'hobbies/hobby-detail.html'


class HobbyCreateView(LoginRequiredMixin, CreateView):
    model = Hobby
    fields = ['name', 'description']
    template_name = 'hobbies/hobby-create.html'


class HobbyUpdateView(LoginRequiredMixin, UpdateView):
    model = Hobby
    fields = ['name', 'description']
    template_name = 'hobbies/hobby-edit.html'


class HobbyDeleteView(LoginRequiredMixin, DeleteView):
    model = Hobby
    template_name = 'hobbies/hobby-delete.html'
    success_url = reverse_lazy('hobbies:hobby-list')