"""Configures the organizer app models to have visibility in the admin interface."""
from django.contrib import admin

from organizer.models import Tag, Startup, NewsLink

admin.site.register(Tag)
admin.site.register(Startup)
admin.site.register(NewsLink)
