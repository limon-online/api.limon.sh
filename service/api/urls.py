from django.urls import include, path

from api.docs import urlpatterns as docs_urls
from api.auth import urlpatterns as auth_urls
from api.user import urlpatterns as users_urls


urlpatterns = [
    path('v1/', include([
        path('docs/', include(docs_urls)),
        path('auth/', include(auth_urls)),
        path('users/', include(users_urls)),
    ]))
]
