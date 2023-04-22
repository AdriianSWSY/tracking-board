from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.board.models import Board, BoardUser


class BoardSerializer(serializers.ModelSerializer):
    """
    Serializer class for Board model.

    Includes creator field, which is a foreign key to the User model and is read-only.
    The creator field is set to the current user when creating a new board in `perform_create` view method.
    """

    creator = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Board
        fields = '__all__'


class BoardUserSerializer(serializers.ModelSerializer):
    """
    Serializer class for BoardUser model.
    """

    class Meta:
        model = BoardUser
        fields = '__all__'
        read_only_fields = ["created", "updated"]  # `created`/`updated` base fields inherited from base model class
