"""Models and model helper functions for the blog app."""
from datetime import date

from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)

from organizer.models import Tag, Startup


class Post(Model):
    """Post model definition."""

    title = CharField(max_length=63)
    slug = SlugField(max_length=63)
    text = TextField()
    pub_date = DateField(
        'date published', default=date.today)
    tags = ManyToManyField(Tag)
    startups = ManyToManyField(Startup)

    class Meta:
        get_latest_by = ['pub_date']
        ordering = ['-pub_date', 'title']
        verbose_name = 'blog post'

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f'{self.title} on {date_string}'
