from django.urls import path

from .views import OrderViewSet

urlpatterns = [
    path("", OrderViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>",
        OrderViewSet.as_view({"patch": "update", "delete": "destroy"}),
    ),
]
