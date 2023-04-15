import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
