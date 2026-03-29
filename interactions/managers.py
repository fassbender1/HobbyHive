from django.db import models


class CommentManager(models.Manager):
    def recent(self):
        return self.order_by('-created_at')