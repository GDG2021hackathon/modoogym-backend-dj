from rest_framework import viewsets

from fitness.models import Fitness
from fitness.serializers import FitnessSerializer


class FitnessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer
