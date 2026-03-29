from django.db import models

from accounts.models import AppUser
from common.validators import validate_min_length, validate_no_special_characters, validate_starts_with_letter
from groups.managers import GroupManager
from hobbies.models import Hobby

class Group(models.Model):
    name = models.CharField(
        max_length=150,
        validators=[
            validate_min_length,
            validate_no_special_characters,
            validate_starts_with_letter
    ]
    )
    description = models.TextField()
    hobby = models.ForeignKey(
        Hobby,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='owned_groups'
    )
    members = models.ManyToManyField(
        AppUser,
        related_name='joined_groups'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    objects = models.Manager()
    custom = GroupManager()

    def members_count(self):
        return self.members.count()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name