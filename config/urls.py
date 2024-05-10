"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import api_root

admin.site.site_header = f"{settings.PROJECT_NAME} Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("my/", include("entries.urls")),
    path("account/", include("customauth.urls.account")),
    # https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints
    path("auth/", include("customauth.urls.base")),
    path("auth/", include("customauth.urls.jwt")),
    path("", api_root.as_view(), name="api-root"),
]
