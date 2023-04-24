import pytest

from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


class TestColumnView:
    """Basic CRUD tests for ColumnView"""

    def test_get_columns_list(self, api_client, factory_user, factory_board, factory_column):
        url = reverse("api:columns:columns-list")
        api_client.force_authenticate(factory_user)

        response = api_client.get(url)
        print('sss', response.data[0])
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['id'] == factory_column.id
        assert response.data[0]["board"] == factory_board.id

    def test_column_create(self, api_client, factory_user, factory_board):
        url = reverse("api:columns:columns-list")
        api_client.force_authenticate(factory_user)

        data = {
            "name": "test",
            "board": factory_board.id
        }

        response = api_client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["board"] == factory_board.id
        assert response.data["name"] == data["name"]
        assert response.data["creator"] == factory_user.id
        assert factory_user.columns.count() == 1

    def test_get_column_detail(self, api_client, factory_user, factory_board, factory_column):
        url = reverse("api:columns:columns-detail", args=(factory_column.id, ))
        api_client.force_authenticate(factory_user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == factory_column.id

    def test_column_delete(self, api_client, factory_user, factory_board, factory_column):
        url = reverse("api:columns:columns-detail", args=(factory_column.id,))
        api_client.force_authenticate(factory_user)

        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not factory_user.columns.exists()

    def test_column_update(self, api_client, factory_user, factory_board, factory_column):
        url = reverse("api:columns:columns-detail", args=(factory_column.id,))
        api_client.force_authenticate(factory_user)

        data = {
            "name": "test1"
        }

        response = api_client.patch(url, data=data)
        factory_column.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == factory_column.name
        assert response.data["name"] == data['name']
