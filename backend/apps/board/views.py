from rest_framework import viewsets, permissions

from apps.board.models import Board
from apps.board.serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with Board objects.

    This viewset provides CRUD operations for Board objects, including creating, reading,
    updating, and deleting Board objects. It uses the BoardSerializer to serialize and
    deserialize Board objects.

    To limit users to making CRUD operations only on their own boards, this viewset overrides
    the `get_queryset` method to return only the boards that belong to the current user.
    """
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return the list of boards that belong to the current user.
        """
        return Board.objects.filter(creator=self.request.user)
