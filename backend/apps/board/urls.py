from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.board.views import BoardViewSet

app_name = "boards"

boards_router = DefaultRouter()
boards_router.register("boards", BoardViewSet, basename="boards")


urlpatterns = [
    path("", include(boards_router.urls)),
]
