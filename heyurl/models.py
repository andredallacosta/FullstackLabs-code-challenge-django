from django.db import models


class Url(models.Model):
    short_url = models.CharField(max_length=255, unique=True)
    original_url = models.CharField(max_length=255, unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')


class Click(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    browser = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
