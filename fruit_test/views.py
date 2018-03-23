from rest_framework import viewsets
from fruit_test.models import Fruits
from fruit_test.serializers import FruitSerializer


class FruitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fruits.objects.all()
    serializer_class = FruitSerializer
