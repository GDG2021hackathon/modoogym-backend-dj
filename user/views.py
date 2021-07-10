from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from membership.models import Membership
from membership.serializers import MyMembershipSerializer
from .serializers import UserSerializer


class MyUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user

        serializer = UserSerializer(user)

        return Response(serializer.data)


class MySaleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user

        my_purchases = Membership.objects.filter(seller=user)

        serializer = MyMembershipSerializer(my_purchases, many=True)
        return Response(serializer.data)


class MyPurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user

        my_purchases = Membership.objects.filter(buyer=user)

        serializer = MyMembershipSerializer(my_purchases, many=True)
        return Response(serializer.data)


class MyFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user

        my_favorites = user.favorites.all()

        serializer = MyMembershipSerializer(my_favorites, many=True)
        return Response(serializer.data)
