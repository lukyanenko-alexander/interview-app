from django.urls import path

from .views import ClientViewSet

urlpatterns = [
    path("", ClientViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>",
        ClientViewSet.as_view({"patch": "update", "delete": "destroy"}),
    ),
]
