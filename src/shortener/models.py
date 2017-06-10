# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from utils import create_shortcode
from django.conf import settings
from .validators import url_validator
from django.core.urlresolvers import reverse
# Create your models here.
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
HOST_NAME = getattr(settings, "HOST_NAME", 'http://127.0.0.1:9000')


class ShortUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=100):
        qs = ShortUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class ShortUrl(models.Model):
    url = models.CharField(max_length=220, validators=[url_validator])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortUrlManager()

    def get_short_url(self):
        url_path = reverse('scode', kwargs={"shortcode": self.shortcode})
        return HOST_NAME + url_path

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
