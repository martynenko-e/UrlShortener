# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import ShortUrl
from .forms import SubmitUrlForm

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Short of url",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Short of url",
            "form": form
        }
        return render(request, "shortener/home.html", context)

# def shortener_redirect_view(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(ShortUrl, shortcode=shortcode)
#     return HttpResponseRedirect(obj.url)


class ShortUrlView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        pass
