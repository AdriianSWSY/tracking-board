from rest_framework import viewsets, permissions

from apps.board.models import Board, BoardUser
from apps.board.serializers import BoardSerializer, BoardUserSerializer


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

    def perform_create(self, serializer):
        serializer.validated_data["creator"] = self.request.user
        return super().perform_create(serializer)


class BoardMemberViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with BoardUser objects.

    This viewset provides CRUD operations for BoardUser objects, including creating, reading,
    updating, and deleting Board objects. It uses the BoardUserSerializer to serialize and
    deserialize BoardUser objects.

    To limit users to making CRUD operations only on their own members, this viewset overrides
    the `get_queryset` method to return only members that belong to user's board.
    """
    serializer_class = BoardUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        """
        Return the list of boards that belong to the current user.
        """
        return BoardUser.objects.filter(board__creator=self.request.user).all()
