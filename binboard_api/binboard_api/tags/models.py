from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    title = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Bundle(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag')
