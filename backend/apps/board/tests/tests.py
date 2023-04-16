import pytest

from django.urls import reverse
from rest_framework import status

from apps.users.models import User

pytestmark = pytest.mark.django_db


class TestBoardView:
    def setup_method(self):
        self.user = User.objects.create(email="test@gmail.com")

    def test_get_boards_list(self, api_client):
        url = reverse("api:boards:boards-list")
        api_client.force_authenticate(self.user)
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_get_boards_detail(self, api_client):
        url = reverse("api:boards:boards-list")
        api_client.force_authenticate(self.user)
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
