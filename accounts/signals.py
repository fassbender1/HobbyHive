from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import AppUser, Profile
from events.tasks import send_event_reminder_async


@receiver(post_save, sender=AppUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        send_event_reminder_async(
            instance.email,
            "Welcome to HobbyHive!"
        )