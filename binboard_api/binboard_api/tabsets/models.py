from django.db import models


class TabSet(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=65536)
    created_at = models.DateTimeField(auto_now_add=True)
    links = models.TextField()
