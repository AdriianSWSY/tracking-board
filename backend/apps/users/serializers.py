from rest_framework import serializers

from dj_rest_auth.serializers import TokenSerializer

from apps.users.models import User


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar', 'role')


class TokenCustomSerializer(TokenSerializer):
    user = UserInfoSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
