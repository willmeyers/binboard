from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from posts.mixins import CreatedAgoMixin


class Note(models.Model, CreatedAgoMixin):
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=65536)
    note_hash = models.CharField(max_length=20)
    shared = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    tags = GenericRelation('tags.Tag')
