from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        contents = {
            "message": "모두의 짐 REST API 입니다!"
        }
        return Response(contents)
