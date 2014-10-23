#!/usr/bin/env python
"""
Contains the web pages related url mappings.
"""

__author__ = "Eraldo Helal"

from django.conf.urls import patterns, url
from django.shortcuts import redirect
from pages.views import HomeView

urlpatterns = patterns('',
    # ex: ../
    # url(r'^$',
    #     lambda x: redirect('home/'),
    #     name='redirect'),
    # ex: ../home/
    url(r'^$',
        HomeView.as_view(),
        name='home'),
)
