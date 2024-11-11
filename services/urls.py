from django.urls import path

from .views import ServiceViewSet

urlpatterns = [
    path("", ServiceViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>",
        ServiceViewSet.as_view({"patch": "update", "delete": "destroy"}),
    ),
]
