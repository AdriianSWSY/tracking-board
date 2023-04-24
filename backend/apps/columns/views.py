from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from apps.columns.models import Column
from apps.columns.serializers import ColumnSerializer


class ColumnViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with BoardUser objects.

    This viewset provides CRUD operations for BoardUser objects, including creating, reading,
    updating, and deleting Board objects. It uses the BoardUserSerializer to serialize and
    deserialize BoardUser objects.

    To limit users to making CRUD operations only on their own members, this viewset overrides
    the `get_queryset` method to return only members that belong to user's board.
    """
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("status", )

    def get_queryset(self):
        """
        Return the list of boards that belong to the current user.
        """
        return Column.objects.filter(Q(board__creator=self.request.user) | Q(board__members=self.request.user))
