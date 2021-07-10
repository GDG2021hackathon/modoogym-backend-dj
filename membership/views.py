from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Membership
from .permissions import IsOwnerOrReadOnly
from .serializers import MembershipSerializer, MyMembershipSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.filter(validation=True)
    serializer_class = MembershipSerializer

    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fitness_id']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    @action(detail=True, methods=['POST'])
    def buy(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]

        membership = self.get_object()
        price = membership.price
        seller = membership.seller
        buyer = self.request.user

        if seller == buyer:
            content = {
                "message": "자신의 상품은 구매할 수 없습니다."
            }
            return Response(content, status=status.HTTP_409_CONFLICT)

        if buyer.cash < price:
            content = {
                "message": "캐쉬가 모자랍니다."
            }
            return Response(content, status=status.HTTP_409_CONFLICT)

        seller.cash += price
        buyer.cash -= price

        membership.buyer = buyer
        membership.validation = False

        seller.save()
        buyer.save()
        membership.save()

        content = {
            "message": "결제가 성공적으로 이루어졌습니다."
        }
        return Response(content, status=status.HTTP_409_CONFLICT)


class MyMembershipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        my_membership = Membership.objects.filter(user=user).order_by("-validation")

        serializer = MyMembershipSerializer(my_membership, many=True)

        return Response(serializer.data)
