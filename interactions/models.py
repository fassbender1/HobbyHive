from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import AppUser
from common.validators import validate_not_empty
from events.models import Event
from groups.models import Group
from interactions.managers import CommentManager


class Comment(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='group_comments'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='event_comments'
    )

    content = models.TextField(
        validators=[validate_not_empty]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    objects = models.Manager()
    custom = CommentManager()

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        if not self.group and not self.event:
            raise ValidationError("Comment must belong to a group or event.")

    def __str__(self):
        return f"Comment by {self.user}"