"""URL paths for Organizer App."""
from django.urls import path

from organizer.views import (
    NewsLinkAPIDetail,
    StartupAPIDetail,
    StartupAPIList,
    TagAPIDetail,
    TagAPIList
)

urlpatterns = [
    path('startup/', StartupAPIList.as_view(),
         name='startup_list'),
    path('startup/<str:slug>/',
         StartupAPIDetail.as_view(), name='api-startup-detail'),
    path('startup/<str:startup_slug>/<str:newslink_slug>/',
         NewsLinkAPIDetail.as_view(), name='api-newslink-detail'),
    path('tag/', TagAPIList.as_view(),
         name='tag_list'),
    path('tag/<str:slug>/',
         TagAPIDetail.as_view(), name='api-tag-detail'),
]
