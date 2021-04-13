from django.http import HttpResponse
from django.urls import include, path

from .v1 import urls as v1_urls


urlpatterns = [
    path('v1/', include(v1_urls)),
    path('healthcheck/', lambda request: HttpResponse(status=200))
]
