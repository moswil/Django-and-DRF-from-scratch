from django.test import TestCase

from .models import Tag


class TagModelTestCase(TestCase):

    def test_create_tag(self):
        name = 'sport'
        # slug = 'sport'
        tag = Tag(name=name)
        self.assertEqual(tag.name, 'sport')
