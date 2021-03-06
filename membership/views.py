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
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fitness_id']

    def list(self, request, *args, **kwargs):
        queryset = Membership.objects.filter(validation=True).exclude(seller=self.request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
        return Response(content)

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]

        membership = self.get_object()

        user = self.request.user
        if membership in user.favorites.all():
            user.favorites.remove(membership)
            user.save()
            content = {
                "message": "좋아요를 취소했습니다."
            }
            return Response(content)

        user.favorites.add(membership)
        user.save()

        content = {
            "message": "좋아요를 추가했습니다."
        }

        return Response(content)


class MyMembershipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        my_membership = Membership.objects.filter(seller=user).order_by("-validation")

        serializer = MyMembershipSerializer(my_membership, many=True)

        return Response(serializer.data)
