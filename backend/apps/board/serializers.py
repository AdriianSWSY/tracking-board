from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.board.models import Board, BoardUser


class BoardSerializer(serializers.ModelSerializer):
    """
    Serializer class for Board model.

    Includes creator field, which is a foreign key to the User model and is read-only.
    The creator field is set to the current user when creating a new board in `perform_create` view method.
    """

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ["created", "updated", "creator"]


class BoardUserSerializer(serializers.ModelSerializer):
    """
    Serializer for BoardUser model.

    This serializer converts BoardUser instances to JSON and vice versa.
    """

    class Meta:
        model = BoardUser
        fields = '__all__'

        # `created` and `updated` fields are inherited from the TimeStampedModel base class and should not be modified.
        read_only_fields = ["created", "updated", "creator"]
