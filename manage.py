#!/usr/bin/env python
import os
import sys
from django import http
from django.conf.urls import url
import app.views 
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personRegister.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

def index(request):
    return http("Hello world!")