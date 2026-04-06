from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
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
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/group-detail.html'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    template_name = 'groups/group-create.html'
    success_url = reverse_lazy('groups:group-list')

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
    success_url = reverse_lazy('groups:group-list')

@login_required
def group_join(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.user not in group.members.all():
        group.members.add(request.user)
        messages.success(request, f'You joined "{group.name}"!')
    else:
        messages.info(request, "You are already in this group.")

    return redirect(group.get_absolute_url())


@login_required
def group_leave(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.user in group.members.all():
        group.members.remove(request.user)
        messages.warning(request, f'You left "{group.name}"!')
    else:
        messages.info(request, "You are not a member.")

    return redirect(group.get_absolute_url())