from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from hobbies.models import Hobby


class HobbyListView(ListView):
    model = Hobby
    template_name = 'hobbies/hobby-list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


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

@login_required
def hobby_join(request, pk):
    hobby = get_object_or_404(Hobby, pk=pk)
    if request.user in hobby.participants.all():
        messages.info(request, f"You already joined '{hobby.name}'.")
    else:
        hobby.participants.add(request.user)
        messages.success(request, f"You joined '{hobby.name}'!")
    return redirect(hobby.get_absolute_url())

@login_required
def hobby_leave(request, pk):
    hobby = get_object_or_404(Hobby, pk=pk)
    if request.user in hobby.participants.all():
        hobby.participants.remove(request.user)
        messages.warning(request, f"You left '{hobby.name}'!")
    else:
        messages.info(request, "You are not participating in this hobby.")
    return redirect(hobby.get_absolute_url())