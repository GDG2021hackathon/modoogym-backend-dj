from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Membership
from .permissions import IsOwnerOrReadOnly
from .serializers import MembershipSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fitness_id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyMembershipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        my_membership = Membership.objects.filter(user=user).order_by("-validation")

        serializer = MembershipSerializer(my_membership, many=True)

        return Response(serializer.data)
