# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ShortUrl
from django.contrib import admin

# Register your models here.


class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortcode', 'get_short_url', 'active']
    list_editable = ['shortcode']


admin.site.register(ShortUrl, ShortUrlAdmin)
