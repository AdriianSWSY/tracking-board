# Starts your fixture name from `factory_` means that it must return an object created by Factory.

import pytest
from rest_framework.test import APIClient, APIRequestFactory

from apps.board.models import Board
from apps.board.tests.factories import BoardFactory
from apps.users.models import User
from apps.users.tests.factories import UserFactory


@pytest.fixture
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def factory_user() -> User:
    """Return a User instance created by UserFactory"""
    return UserFactory()


@pytest.fixture
def factory_board(factory_user) -> Board:
    """Return a Board instance created by BoardFactory"""
    return BoardFactory(creator=factory_user)

