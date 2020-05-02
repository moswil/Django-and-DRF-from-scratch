"""Viewsets for the Blog App."""
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """A set of views for the Post model."""

    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        """Override DRF's generic method."""
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
