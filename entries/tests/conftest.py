import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def _do_authenticate():
        user = baker.make(User)
        api_client.force_authenticate(user=user)

    return _do_authenticate
