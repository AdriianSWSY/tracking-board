from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.board.views import BoardViewSet, BoardMemberViewSet

app_name = "columns"

columns_router = DefaultRouter()
columns_router.register("columns", BoardViewSet, basename="columns")

urlpatterns = [
    path("", include(columns_router.urls)),
]
