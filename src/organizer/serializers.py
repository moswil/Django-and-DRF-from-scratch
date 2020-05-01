"""Serializers for the Organizer App."""
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField
)

from organizer.models import NewsLink, Startup, Tag


class TagSerializer(HyperlinkedModelSerializer):
    """Serialize Tag data."""

    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
                'view_name': 'api-tag-detail'
            }
        }


class StartupSerializer(HyperlinkedModelSerializer):
    """Serialize startup data."""

    tags = HyperlinkedRelatedField(
        lookup_field='slug',
        many=True,
        read_only=True,
        view_name='api-tag-detail'
    )

    class Meta:
        model = Startup
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
                'view_name': 'api-startup-detail'
            }
        }


class NewLinkSerializer(ModelSerializer):
    """Serialize NewsLink data."""

    url = SerializerMethodField()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field='slug',
        view_name='api-startup-detail'
    )

    class Meta:
        model = NewsLink
        exclude = ('id',)

    def get_url(self, newslink):
        """Build full URL for NewsLink API detail."""
        return reverse(
            "api-newslink-detail",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug
            ),
            request=self.context['request']
        )
