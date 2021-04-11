from rest_framework import viewsets, status, response, decorators


class AuthenticationViewSet(viewsets.ViewSet):
    @decorators.action(
        detail=False,
        methods=['post']
    )
    def sign_up(self, *args, **kwargs):
        """
        Sign up

        Sign up a new user and send confirmation email.
        """

        return response.Response(status=status.HTTP_201_CREATED)
