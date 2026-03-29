from django.db import models


class GroupManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def by_user(self, user):
        return self.filter(owner=user)