from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.board.models import Board


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
