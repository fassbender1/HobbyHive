from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    email = models.EmailField(
        unique=True
    )

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE
    )
    bio = models.TextField(
        blank=True
    )
    profile_picture = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"