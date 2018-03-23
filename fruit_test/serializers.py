from rest_framework import serializers
from fruit_test.models import Fruits


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = ('id', 'name', 'price', 'image', 'created')
