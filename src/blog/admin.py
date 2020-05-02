"""Configures the blog app models to have visibility in the admin interface."""
from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Blog Posts model view in the admin interface."""

    list_display = ('title', 'slug', 'pub_date')
