#!/usr/bin/env python
"""
This module contains the web pages based views.
"""
from django.contrib import messages
from django.views.generic import TemplateView

__author__ = "Eraldo Helal"


class HomeView(TemplateView):
    template_name = "pages/home.html"
