from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.columns.views import ColumnViewSet

app_name = "columns"

columns_router = DefaultRouter()
columns_router.register("columns", ColumnViewSet, basename="columns")

urlpatterns = [
    path("", include(columns_router.urls)),
]
