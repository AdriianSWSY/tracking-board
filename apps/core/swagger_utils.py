from drf_yasg.openapi import Schema, TYPE_STRING, TYPE_OBJECT
from rest_framework import serializers

from apps.users.serializers import UserInfoSerializer

social_auth_schema = Schema(
    properties={'access_token': Schema(type=TYPE_STRING),
                'code': Schema(type=TYPE_STRING)},
    type=TYPE_OBJECT
)


class AuthResponseSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    user = UserInfoSerializer(required=True)
