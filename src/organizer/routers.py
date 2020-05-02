"""URL Paths and Routers for Organizer App."""
from rest_framework.routers import SimpleRouter

from organizer.viewsets import (
    NewsLinkViewSet,
    StartupViewSet,
    TagViewSet
)


class NewsLinkRouter(SimpleRouter):
    """Overides the SimpleRouter for articles.

    DRF's routers expect there to only be a single variable
    for finding objects. However, our NewsLinks needs two.
    We therefore override the Router's behaviour to make it
    do what we want.

    The big question: was it worth switching to a ViewSet and
    Router over our previous config for this?
    """

    def get_lookup_regex(self, *args, **kwargs):
        """Return a regular expression pattern for URL path.

        This is the (rough) equivalent of the simple path:
            <str:startup_slug>/<str:newslink_slug>
        """
        return (
            r'(?P<startup_slug>[^/.]+)/'
            r'(?P<newslink_slug>[^/.]+)'
        )


api_router = SimpleRouter()
api_router.register('tag', TagViewSet, basename='api-tag')
api_router.register(
    'startup', StartupViewSet, basename='api-startup')

nl_router = NewsLinkRouter()
nl_router.register(
    'newslink', NewsLinkViewSet, basename='api-newslink')

urlpatterns = api_router.urls + nl_router.urls
