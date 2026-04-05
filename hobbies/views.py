from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
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

def hobby_join(request, pk):
    hobby = get_object_or_404(Hobby, pk=pk)
    hobby.participants.add(request.user)
    messages.success(request, f'You joined the hobby "{hobby.name}"!')
    return redirect(hobby.get_absolute_url())

def hobby_leave(request, pk):
    hobby = get_object_or_404(Hobby, pk=pk)
    hobby.participants.remove(request.user)
    messages.warning(request, f'You left the hobby "{hobby.name}"!')
    return redirect(hobby.get_absolute_url())