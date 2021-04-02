from django.urls import path

from apps.user.views import UserView, ProfileView, ProfileAvatarView

urlpatterns = [
    path('current/', UserView.as_view()),
    path('current/profile/', ProfileView.as_view()),
    path('current/profile/avatar/', ProfileAvatarView.as_view()),
]
