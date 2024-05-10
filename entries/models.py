from uuid import uuid4

from django.conf import settings
from django.db import models
from django_cryptography.fields import encrypt


class Entry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = encrypt(models.CharField(max_length=255))
    username = encrypt(models.CharField(max_length=255))
    password = encrypt(models.CharField(max_length=255))
    url = encrypt(models.URLField(max_length=255, null=True, blank=True))
    notes = encrypt(models.TextField(null=True, blank=True))

    class Meta:
        db_table = "entries"
