import pytest

from django.urls import reverse
from rest_framework import status

from apps.users.models import User

pytestmark = pytest.mark.django_db


class TestBoardView:
    """Basic CRUD tests for BoardView"""

    def test_get_boards_list(self, api_client, factory_user, factory_board):
        url = reverse("api:boards:boards-list")
        api_client.force_authenticate(factory_user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['id'] == str(factory_board.id)

    def test_get_boards_create(self, api_client, factory_user, factory_board):
        url = reverse("api:boards:boards-list")
        api_client.force_authenticate(factory_user)

        data = {
            "name": "test",
            "description": "test description"
        }

        response = api_client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] != str(factory_board.id)
        assert response.data["name"] == data["name"]
        assert factory_user.boards.count() == 2

    def test_get_boards_detail(self, api_client, factory_user, factory_board):
        url = reverse("api:boards:boards-detail", args=(factory_board.id, ))
        api_client.force_authenticate(factory_user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == str(factory_board.id)

    def test_get_boards_delete(self, api_client, factory_user, factory_board):
        url = reverse("api:boards:boards-detail", args=(factory_board.id,))
        api_client.force_authenticate(factory_user)

        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not factory_user.boards.exists()

    def test_get_boards_update(self, api_client, factory_user, factory_board):
        url = reverse("api:boards:boards-detail", args=(factory_board.id,))
        api_client.force_authenticate(factory_user)

        data = {
            "name": "test"
        }

        response = api_client.patch(url, data=data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] != factory_board.name
