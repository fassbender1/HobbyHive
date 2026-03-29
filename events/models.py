from django.db import models

from accounts.choices import EVENT_STATUS_CHOICES
from accounts.models import AppUser
from common.validators import validate_future_date
from events.managers import EventManager
from groups.models import Group


class Event(models.Model):
    title = models.CharField(
        max_length=150
    )
    description = models.TextField()

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='events'
    )
    organizer = models.ForeignKey(
        AppUser, on_delete=models.CASCADE,
        related_name='organized_events'
    )

    date = models.DateTimeField(
        validators=[validate_future_date]
    )

    location = models.CharField(
        max_length=255
    )

    class Meta:
        ordering = ['date']

    def participants_count(self):
        return self.participants.count()

    def __str__(self):
        return self.title

    objects = models.Manager()
    custom = EventManager()


class EventParticipation(models.Model):

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='event_participations'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    status = models.CharField(
        max_length=20,
        choices=EVENT_STATUS_CHOICES,
    )

    def is_going(self):
        return self.status == 'going'

    class Meta:
        ordering = ['-id']
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user} -> {self.event} ({self.status})"
