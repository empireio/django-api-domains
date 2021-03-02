import uuid

from django.db import models


class Article(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    author_guid = models.UUIDField(default=uuid.uuid4)
