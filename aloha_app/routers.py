from rest_framework.routers import DefaultRouter
from backend_mobile.user import viewsets as users_views
from backend_mobile.records import viewsets as records_views

router = DefaultRouter()

router.register("user", users_views.UserViewSet, base_name="user")
router.register("galery", records_views.GaleryViewSet, base_name="galery")
