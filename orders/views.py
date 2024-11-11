from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from orders.models import Order


class OrderServiceSerializer:
    pass

class OrderCreateSerializer(serializers.ModelSerializer):
    pass


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer