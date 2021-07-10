import requests
from django.conf import settings
from django.contrib.auth.models import update_last_login
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from user.models import User


def create_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def login_by_social(email):
    user = User.objects.get(email=email)
    return user


def register_by_social(email, nickname):
    user = User.objects.create_user(email=email, nickname=nickname)

    return user


def naver_login(request):
    naver_client_id = getattr(settings, 'NAVER_CLIENT_ID', None)
    redirect_uri = "http://localhost:8000/auth/naver/login/callback/"
    print(
        f"https://nid.naver.com/oauth2.0/authorize?client_id={naver_client_id}&redirect_uri={redirect_uri}&response_type=code")
    return redirect(
        f"https://nid.naver.com/oauth2.0/authorize?client_id={naver_client_id}&redirect_uri={redirect_uri}&response_type=code"
    )


@api_view(['POST'])
def naver_callback(request):
    try:
        naver_client_id = getattr(settings, 'NAVER_CLIENT_ID', None)
        naver_client_secret = getattr(settings, 'NAVER_CLIENT_SECRET', None)
        user_token = request.data.get("code")
        state = request.data.get("state", "")
        # post request
        token_request = requests.get(
            f"https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={naver_client_id}&client_secret={naver_client_secret}&code={user_token}&state={state}"
        )
        token_response_json = token_request.json()
        error = token_response_json.get("error", None)

        # if there is an error from token_request
        if error is not None:
            raise Exception
        access_token = token_response_json.get("access_token")

        # post request
        profile_request = requests.post(
            "https://openapi.naver.com/v1/nid/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        # parsing profile json
        naver_account = profile_json.get("response")
        email = naver_account.get("email")
        try:
            user = login_by_social(email)
        except User.DoesNotExist:
            nickname = naver_account.get("nickname")
            user = register_by_social(email, nickname)

        update_last_login(None, user)

        token = create_token(user)
        headers = {"Token": token}

        content = {
            "message": "로그인에 성공했습니다"
        }
        return Response(content, headers=headers)
    except Exception as e:
        content = {
            "message": str(e)
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
