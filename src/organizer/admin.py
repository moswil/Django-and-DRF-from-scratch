"""Configures the organizer app models to have visibility in the admin interface."""
from django.contrib import admin

from organizer.models import Tag, Startup, NewsLink

admin.site.register(NewsLink)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Customized admin view of the tag model."""

    list_display = ('name', 'slug')


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    """Customized admin view of the startup model."""

    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
