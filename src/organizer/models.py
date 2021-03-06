"""Django data models for organizing startup company data"""
from django_extensions.db.fields import AutoSlugField
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    URLField,
)


class Tag(Model):
    """Label to help categorize the data."""

    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        max_length=31, help_text="A label for URL config", populate_from=['name'])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Startup(Model):
    """Data about a startup company."""

    name = CharField(max_length=31, db_index=True)
    slug = SlugField(
        max_length=31, help_text="A label for URL config", unique=True)
    description = TextField()
    founded_date = DateField('date founded')
    contact = EmailField()
    website = URLField(max_length=255)
    tags = ManyToManyField(Tag)

    class Meta:
        get_latest_by = ['founded_date']
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class NewsLink(Model):
    """newslink model fields."""

    title = CharField(max_length=31)
    slug = SlugField(max_length=31)
    pub_date = DateField('date published')
    link = URLField(max_length=255)
    startup = ForeignKey(
        Startup, on_delete=CASCADE)

    class Meta:
        get_latest_by = ['pub_date']
        ordering = ['-pub_date']
        unique_together = ('slug', 'startup')
        verbose_name = 'news article'

    def __str__(self):
        return f'{self.startup}: {self.title}'
