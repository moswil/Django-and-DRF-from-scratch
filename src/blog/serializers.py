"""Serializers for the Blog App."""
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField
)

from blog.models import Post
from organizer.models import Startup, Tag


class PostSerializer(ModelSerializer):
    """Serialize post data"""

    url = SerializerMethodField()
    tags = HyperlinkedRelatedField(
        lookup_field='slug',
        many=True,
        queryset=Tag.objects.all(),
        view_name='api-tag-detail'
    )
    startups = HyperlinkedRelatedField(
        lookup_field='slug',
        many=True,
        queryset=Startup.objects.all(),
        view_name='api-startup-detail'
    )

    class Meta:
        model = Post
        exclude = ('id',)

    def get_url(self, post):
        """Return full API URL for serialized POST object."""
        return reverse(
            'api-post-detail',
            kwargs=dict(
                year=post.pub_date.year,
                month=post.pub_date.month,
                slug=post.slug
            ),
            request=self.context['request']
        )
