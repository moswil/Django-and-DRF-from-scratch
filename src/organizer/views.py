"""Views for the Organizer App"""
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)

from organizer.models import NewsLink, Startup, Tag
from organizer.serializers import (
    NewLinkSerializer,
    StartupSerializer,
    TagSerializer
)


class TagAPIList(ListCreateAPIView):
    """Display a list of Tags. And allows creation of a tag on POST"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagAPIDetail(RetrieveUpdateDestroyAPIView):
    """Display a single Tag. And updates an exisiting tag on PUT/PATCH"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class StartupAPIList(ListAPIView):
    """Display a list of Startups."""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = 'slug'


class StartupAPIDetail(RetrieveAPIView):
    """Display a single Startup."""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class NewsLinkAPIDetail(RetrieveAPIView):
    """Returns a JSON for a single NewsLink object."""

    queryset = NewsLink.objects.all()
    serializer_class = NewLinkSerializer

    def get_object(self):
        """Overides the DRF's generic method."""
        startup_slug = self.kwargs.get('startup_slug')
        newslink_slug = self.kwargs.get('newslink_slug')

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug
        )
        self.check_object_permissions(
            self.request, newslink)

        return newslink
