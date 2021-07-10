from django.urls import path

from .views import MyUserView

urlpatterns = [
    path("my/", MyUserView.as_view()),
]
