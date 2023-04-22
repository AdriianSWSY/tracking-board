import pytest

from django.urls import reverse
from rest_framework import status

from apps.board.enums import BoardUserRole
from apps.board.models import BoardUser
from apps.board.tests.factories import BoardUserFactory
from apps.users.models import User
from apps.users.tests.factories import UserFactory

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


class TestBoardUserView:
    """Basic CRUD tests for BoardUserView"""

    def test_get_members_list(self, api_client, factory_user, factory_board):
        members = BoardUserFactory(board=factory_board)

        url = reverse("api:boards:members-list")
        api_client.force_authenticate(factory_user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['id'] == members.id

    def test_member_create(self, api_client, factory_user, factory_board):
        url = reverse("api:boards:members-list")
        api_client.force_authenticate(factory_user)

        data = {
            "user": UserFactory().id,
            "board": factory_board.id
        }

        response = api_client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["board"] == factory_board.id
        assert factory_board.members.count() == 1

    def test_get_members_detail(self, api_client, factory_user, factory_board, factory_member):
        url = reverse("api:boards:members-detail", args=(factory_member.id, ))
        api_client.force_authenticate(factory_user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['board'] == factory_board.id
        assert response.data['id'] == factory_member.id
        assert response.data['user'] == factory_member.user.id

    def test_member_delete(self, api_client, factory_user, factory_board, factory_member):
        url = reverse("api:boards:members-detail", args=(factory_member.id,))
        api_client.force_authenticate(factory_user)

        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not factory_board.members.exists()

    def test_member_update(self, api_client, factory_user, factory_board, factory_member):
        url = reverse("api:boards:members-detail", args=(factory_member.id,))
        api_client.force_authenticate(factory_user)

        data = {
            "role": BoardUserRole.admin,
        }

        response = api_client.patch(url, data=data)
        factory_member.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert response.data["role"] == factory_member.role
