"""URL paths for the Blog App."""
from django.urls import path

from blog.views import PostAPIDetail, PostAPIList

urlpatterns = [
    path('blog/', PostAPIList.as_view(),
         name='api-post-list'),
    path('blog/<int:year>/<int:month>/<str:slug>/', PostAPIDetail.as_view(),
         name='api-post-detail'),
]
