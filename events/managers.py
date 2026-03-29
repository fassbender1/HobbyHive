from django.db import models


class EventManager(models.Manager):
    def upcoming(self):
        from django.utils.timezone import now
        return self.filter(date__gte=now())

    def by_user(self, user):
        return self.filter(organizer=user)