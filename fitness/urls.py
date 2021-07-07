from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FitnessViewSet

router = DefaultRouter()
router.register("", FitnessViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
