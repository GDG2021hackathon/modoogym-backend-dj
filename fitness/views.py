from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from fitness.models import Fitness
from fitness.serializers import FitnessSerializer


class FitnessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['location_id', 'category_id']
