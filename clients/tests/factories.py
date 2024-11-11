import factory

from clients.models import Client


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    name = "Bogdan"
