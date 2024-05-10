from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class api_root(APIView):
    def get(self, request):
        endpoints = {
            # "": reverse("", request=request,),
            "create-account": {
                "sign-up": reverse(
                    "customuser-list",
                    request=request,
                ),
                "activation": reverse(
                    "customuser-activation",
                    request=request,
                ),
                "resend-activation": reverse(
                    "customuser-resend-activation",
                    request=request,
                ),
            },
            "authentication": {
                "sign-in": reverse(
                    "jwt-create",
                    request=request,
                ),
                "token-refresh": reverse(
                    "jwt-refresh",
                    request=request,
                ),
                "token-verify": reverse(
                    "jwt-verify",
                    request=request,
                ),
            },
            "database": {
                "my-database": reverse(
                    "database-list",
                    request=request,
                ),
            },
            "profile": {
                "profile": reverse(
                    "customuser-me",
                    request=request,
                ),
            },
            "password-management": {
                "set-password": reverse(
                    "customuser-set-password",
                    request=request,
                ),
                "reset-password": reverse(
                    "customuser-reset-password",
                    request=request,
                ),
                "reset-password-confirm": reverse(
                    "customuser-reset-password-confirm",
                    request=request,
                ),
            },
            "email-management": {
                "set-email": reverse(
                    "customuser-set-username",
                    request=request,
                ),
                "reset-email": reverse(
                    "customuser-reset-username",
                    request=request,
                ),
                "reset-email-confirm": reverse(
                    "customuser-reset-username-confirm",
                    request=request,
                ),
            },
        }
        return Response(endpoints, status=status.HTTP_200_OK)
