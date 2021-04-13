from django.urls import include, path

from .auth.urls import urlpatterns as auth_urls
from .docs.urls import urlpatterns as docs_urls


urlpatterns = [
    path('docs/', include(docs_urls)),
    path('auth/', include(auth_urls))
]
