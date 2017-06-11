# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import ShortUrl
from .forms import SubmitUrlForm
from analytics.models import ClickEvent

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Short that url",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Short of url",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = ShortUrl.objects.get_or_create(url=new_url)
            context = {
                "form": form,
                "url": obj.url,
                "short_url": obj.get_short_url(),
                "created": created
            }
            if created:
                context.update({"title_text": "Success! Shortlink created!"})
                template = "shortener/success.html"
            else:
                context.update({"title_text": "Success! Shortlink created!"})
                template = "shortener/already-exists.html"
        else:
            context.update({"form_valid": False})
        return render(request, template, context)


class ShortUrlView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, shortcode__iexact=shortcode)
        # save item
        print ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        raise Http404
