from rest_framework import viewsets, status, response, decorators, permissions
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User
from .serializers import SignUpSerializer


class AuthenticationViewSet(viewsets.ViewSet):
    @decorators.action(
        detail=False,
        methods=['post'],
        url_path='sign-up',
        permission_classes=[
            permissions.AllowAny
        ]
    )
    def sign_up(self, *args, **kwargs):
        """
        Sign up

        Sign up a new user and send confirmation email.
        """

        serializer = SignUpSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        refresh = RefreshToken.for_user(
            User.objects.create_user(**serializer.validated_data)
        )

        return response.Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED
        )
