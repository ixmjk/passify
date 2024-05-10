from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.include_root_view = False
router.register("database", views.EntryViewSet, basename="database")

urlpatterns = router.urls
