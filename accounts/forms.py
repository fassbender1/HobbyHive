from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')

        error_messages = {
            'username': {'required': 'Username is required!'},
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disabled example ✔
        if self.instance and self.instance.user:
            self.fields['bio'].help_text = "Tell others about yourself"