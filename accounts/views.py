from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from accounts.forms import RegisterForm
from accounts.models import Profile, AppUser
from django.contrib.auth.views import LoginView, LogoutView
from events.models import Event

UserModel = get_user_model()

class RegisterView(CreateView):
    model = AppUser
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Welcome! Your account has been created.")
        return response

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['participated_events'] = Event.objects.filter(
            participants__user=user
        )

        context['joined_groups'] = user.joined_groups.all()
        context['joined_hobbies'] = user.joined_hobbies.all()

        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['bio', 'profile_picture']
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile-detail', kwargs={'pk': self.object.pk})

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('common:home')

    def get_object(self, queryset=None):
        return self.request.user

class UserListView(LoginRequiredMixin, ListView):
    model = AppUser
    template_name = 'accounts/user-list.html'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        messages.success(self.request, f"Welcome back, {self.request.user.username}!")
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('common:home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)