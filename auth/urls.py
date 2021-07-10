from django.urls import path

from .views import (
    naver_login, naver_callback
)

urlpatterns = [
    path('naver/login/', naver_login),
    path('naver/login/callback/', naver_callback),
    # path('naver/login/access/', naver_access),
]
