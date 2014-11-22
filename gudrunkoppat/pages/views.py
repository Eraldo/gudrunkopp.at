#!/usr/bin/env python
"""
This module contains the web pages based views.
"""
from django.contrib import messages
from django.views.generic import TemplateView
from pages.models import Block

__author__ = "Eraldo Helal"


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['slogan'] = self.get_block("Slogan")
        context['person'] = self.get_block("Person")
        context['children'] = self.get_block("Kinder")
        context['parents'] = self.get_block("Eltern")
        context['supervision'] = self.get_block("Supervision")
        context['coaching'] = self.get_block("Coaching")
        context['lead'] = self.get_block("Erstkontakt")
        context['contact'] = self.get_block("Kontakt")
        return context

    @staticmethod
    def get_block(name):
        try:
            block = Block.objects.get(name=name).description
        except Block.DoesNotExist:
            block = ""
        return block
