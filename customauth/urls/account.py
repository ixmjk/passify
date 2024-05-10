from django.urls import path

from customauth import views

urlpatterns = [
    path("activate/<str:uid>/<str:token>", views.activate),
    path("reset-password/<str:uid>/<str:token>", views.reset_password),
    path("reset-email/<str:uid>/<str:token>", views.reset_email),
]
