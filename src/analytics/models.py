# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shortener.models import ShortUrl
# Create your models here.


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortUrl):
            obj, created = self.get_or_create(short_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        else:
            return None


class ClickEvent(models.Model):
    short_url = models.OneToOneField(ShortUrl, related_name="clickevent")
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)  # last clicked
    timestamp = models.DateTimeField(auto_now_add=True)  # first click

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
