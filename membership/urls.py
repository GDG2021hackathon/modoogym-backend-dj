from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MembershipViewSet, MyMembershipView

router = DefaultRouter()
router.register("", MembershipViewSet)

urlpatterns = [
    path("my/", MyMembershipView.as_view()),
    path("", include(router.urls)),
]
