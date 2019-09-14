from rest_framework.routers import DefaultRouter
from backend_mobile.user import viewsets as users_views

router = DefaultRouter()

router.register("user", users_views.UserViewSet, base_name="user")
