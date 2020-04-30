# Generated by Django 3.0.5 on 2020-04-30 00:18

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config', max_length=31, populate_from=['name']),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config', max_length=31, populate_from=['name']),
        ),
    ]
