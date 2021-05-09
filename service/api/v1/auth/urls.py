from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import AuthenticationViewSet


router = routers.SimpleRouter()
router.register('', AuthenticationViewSet, basename='Authentication')

urlpatterns = [
    *router.urls,

    # TODO: Make token view as part of AuthenticationViewSet
    path('token/', TokenObtainPairView.as_view())
]
