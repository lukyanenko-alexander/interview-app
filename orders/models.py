from django.db import models

from services.models import Service


class OrderQuerySet(models.QuerySet):
    def with_services(self):
        pass

class Order(models.Model):
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default="")
    services = models.ManyToManyField("services.Service", through="orders.OrderService")

    objects = OrderQuerySet.as_manager()


class OrderService(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.TextField(default="")