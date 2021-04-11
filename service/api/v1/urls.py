from django.urls import include, path

from .auth.urls import urlpatterns as auth_urls


urlpatterns = [
    path('auth', include(auth_urls))
]
