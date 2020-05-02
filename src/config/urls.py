"""config URL Configuration"""
from django.contrib import admin
from django.urls import path, include

# from organizer.urls import urlpatterns as organizer_urls
# from blog.urls import urlpatterns as blog_urls

from blog.routers import urlpatterns as blog_api_urls
from organizer.routers import urlpatterns as organizer_api_urls

api_urls = blog_api_urls + organizer_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]
