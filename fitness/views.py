from rest_framework import viewsets, filters

from fitness.models import Fitness
from fitness.serializers import FitnessSerializer


class FitnessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
