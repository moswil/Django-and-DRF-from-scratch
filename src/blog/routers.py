"""URL Paths and Routers for the Blog App."""
from rest_framework.routers import SimpleRouter

from blog.viewsets import PostViewSet


class PostRouter(SimpleRouter):
    """Override the SimpleRouter for blog posts.

    DRF's routers expect there to only be a single variable
    for finding objets. However, our blog posts needs three!
    We therefore override the Router's behaviour to make it
    do what we want.

    The biggest question: was it worth switching to a ViewSet and Router over our previous config for this?
    """

    def get_lookup_regex(self, *args, **kwargs):
        """Return regular expression pattern for URL path.

        This is the equivalent of the simple path:
            <int:year>/<int:month>/<str:slug>
        """
        return (
            r'(?P<year>\d+)/'
            r'(?P<month>\d+)/'
            r'(?P<slug>[\w\-]+)'
        )


api_routers = PostRouter()
api_routers.register(
    'blog', PostViewSet, basename='api-post')

urlpatterns = api_routers.urls
