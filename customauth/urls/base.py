from django.contrib.auth import get_user_model

# from djoser import views
from rest_framework.routers import DefaultRouter

from customauth import views

router = DefaultRouter()
router.include_root_view = False
router.register("users", views.UserViewSet)

User = get_user_model()

urlpatterns = router.urls
