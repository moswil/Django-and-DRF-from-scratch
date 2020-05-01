"""Views for the Blog App."""
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from blog.models import Post
from blog.serializers import PostSerializer


class PostAPIList(ListAPIView):
    """Returns a list of all blog posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetail(RetrieveAPIView):
    """Return a single Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        """Overides the DRF's get_object."""
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        slug = self.kwargs.get('slug')

        queryset = self.filter_queryset(self.get_queryset())

        post = get_object_or_404(
            queryset,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug
        )

        self.check_object_permissions(self.request, post)

        return post
