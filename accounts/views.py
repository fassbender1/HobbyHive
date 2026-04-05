from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from accounts.forms import RegisterForm
from accounts.models import Profile, AppUser
from django.contrib.auth.views import LoginView, LogoutView

UserModel = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-detail.html'

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

class UserLogoutView(LogoutView):
    next_page = '/'