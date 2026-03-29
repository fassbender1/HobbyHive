from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Group
from .forms import GroupCreateForm, GroupUpdateForm, GroupDeleteForm
from common.mixins import OwnerRequiredMixin

class GroupListView(ListView):
    model = Group
    template_name = 'groups/group-list.html'
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/group-detail.html'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    template_name = 'groups/group-create.html'
    success_url = reverse_lazy('group-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GroupUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'groups/group-edit.html'

class GroupDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/group-delete.html'
    success_url = reverse_lazy('group-list')