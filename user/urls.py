from django.urls import path

from .views import MyUserView, MySaleView, MyPurchaseView

urlpatterns = [
    path("my/sales/", MySaleView.as_view()),
    path("my/purchases/", MyPurchaseView.as_view()),
    path("my/", MyUserView.as_view()),
]
