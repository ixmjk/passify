from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils import timezone
from djoser.conf import settings
from djoser.views import UserViewSet as BaseUserViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView as BaseTokenVerifyView

from .throttles import AnonRateThrottle, UserRateThrottle

User = get_user_model()


def activate(request, uid, token):
    return render(
        request,
        "account/activate.html",
        context={
            "title": "Activate Account",
            "uid": uid,
            "token": token,
        },
    )


def reset_password(request, uid, token):
    return render(
        request,
        "account/reset_password.html",
        context={
            "title": "Reset Password",
            "uid": uid,
            "token": token,
        },
    )


def reset_email(request, uid, token):
    return render(
        request,
        "account/reset_email.html",
        context={
            "title": "Reset Email",
            "uid": uid,
            "token": token,
        },
    )


class TokenObtainPairView(BaseTokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            if settings.SEND_NEW_SIGN_IN_EMAIL:
                current_datetime = timezone.now()
                context = {
                    "user": request.data.get("email"),
                    "device": "{browser} on {os} {version}".format(
                        browser=self.request.user_agent.browser.family,
                        os=self.request.user_agent.os.family,
                        version=self.request.user_agent.os.version_string,
                    ),
                    "date": current_datetime.strftime("%A, %b %d, %Y"),
                    "time": current_datetime.strftime("%I:%M:%S %p (%Z)"),
                }
                to = [request.data.get("email")]
                settings.EMAIL.new_sign_in(self.request, context).send(to)

        return response


class TokenRefreshView(BaseTokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            if settings.SEND_NEW_SIGN_IN_EMAIL:
                current_datetime = timezone.now()
                context = {
                    "user": request.data.get("email"),
                    "device": "{browser} on {os} {version}".format(
                        browser=self.request.user_agent.browser.family,
                        os=self.request.user_agent.os.family,
                        version=self.request.user_agent.os.version_string,
                    ),
                    "date": current_datetime.strftime("%A, %b %d, %Y"),
                    "time": current_datetime.strftime("%I:%M:%S %p (%Z)"),
                }
                to = [request.data.get("email")]
                settings.EMAIL.new_sign_in(self.request, context).send(to)

        return response


class TokenVerifyView(BaseTokenVerifyView):
    pass


class UserViewSet(BaseUserViewSet):
    @action(
        ["post"],
        detail=False,
        throttle_classes=[AnonRateThrottle, UserRateThrottle],
    )
    def resend_activation(self, request, *args, **kwargs):
        return super().resend_activation(request, *args, **kwargs)

    @action(
        ["post"],
        detail=False,
        throttle_classes=[AnonRateThrottle, UserRateThrottle],
    )
    def reset_password(self, request, *args, **kwargs):
        return super().reset_password(request, *args, **kwargs)

    @action(
        ["post"],
        detail=False,
        url_path=f"reset_{User.USERNAME_FIELD}",
        throttle_classes=[AnonRateThrottle, UserRateThrottle],
    )
    def reset_username(self, request, *args, **kwargs):
        return super().reset_username(request, *args, **kwargs)
