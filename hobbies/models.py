from django.db import models
from django.urls import reverse

from accounts.models import AppUser


class Hobby(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        blank=True
    )

    participants = models.ManyToManyField(
        AppUser,
        related_name='joined_hobbies',
        blank=True
    )

    owner = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='owned_hobbies',
        default=None,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('hobbies:hobby-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name