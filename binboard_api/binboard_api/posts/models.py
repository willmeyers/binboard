import datetime
from django.db import models

from .mixins import CreatedAgoMixin


class Post(models.Model, CreatedAgoMixin):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=65536)
    replace = models.BooleanField(default=True)
    shared = models.BooleanField(default=True)
    starred = models.BooleanField(default=False)
    toread = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
