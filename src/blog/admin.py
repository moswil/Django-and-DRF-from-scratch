"""Configures the blog app models to have visibility in the admin interface."""
from django.contrib import admin

from blog.models import Post

admin.site.register(Post)
