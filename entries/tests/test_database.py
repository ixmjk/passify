import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework import status

from entries.models import Entry

User = get_user_model()


@pytest.fixture
def create_entry(api_client):
    def _do_create_entry(entry):
        return api_client.post("/my/database/", entry)

    return _do_create_entry


@pytest.fixture
def retrieve_entry_list(api_client):
    def _do_retrieve_entry_list():
        return api_client.get("/my/database/")

    return _do_retrieve_entry_list


@pytest.fixture
def retrieve_entry(api_client):
    def _do_retrieve_entry(id):
        return api_client.get(f"/my/database/{id}/")

    return _do_retrieve_entry


@pytest.fixture
def delete_entry(api_client):
    def _do_delete_entry(id):
        return api_client.delete(f"/my/database/{id}/")

    return _do_delete_entry


@pytest.fixture
def update_entry(api_client):
    def _do_update_entry(id, updated_entry):
        return api_client.put(f"/my/database/{id}/", updated_entry)

    return _do_update_entry


@pytest.fixture
def partial_update_entry(api_client):
    def _do_partial_update_entry(id, updated_entry):
        return api_client.patch(f"/my/database/{id}/", updated_entry)

    return _do_partial_update_entry


@pytest.fixture
def save_entry():
    def _do_save_entry(
        user_id=None,
        title="a",
        username="a",
        password="a",
    ):
        return Entry.objects.create(
            user_id=user_id,
            title="a",
            username="a",
            password="a",
        )

    return _do_save_entry


@pytest.mark.django_db
class TestCreateEntry:
    def test_if_user_is_anonymous_returns_401(self, create_entry):
        response = create_entry({})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_invalid_returns_400(self, authenticate, create_entry):
        authenticate()

        response = create_entry({})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_entry):
        authenticate()

        response = create_entry(
            {
                "title": "a",
                "username": "a",
                "password": "a",
                "url": "",
                "notes": "",
            },
        )

        print(response.data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == "a"


@pytest.mark.django_db
class TestRetrieveEntryList:
    def test_if_user_is_anonymous_returns_401(self, retrieve_entry_list):
        response = retrieve_entry_list()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["detail"] is not None

    def test_if_user_is_authenticated_returns_200(
        self, authenticate, retrieve_entry_list
    ):
        authenticate()

        response = retrieve_entry_list()

        assert response.status_code == status.HTTP_200_OK
        assert response.data == []


@pytest.mark.django_db
class TestRetrieveEntry:
    def test_if_user_is_anonymous_returns_401(self, save_entry, retrieve_entry):
        response = retrieve_entry("a")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_entry_id_is_invalid_returns_404(self, authenticate, retrieve_entry):
        authenticate()

        response = retrieve_entry("a")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_entry_id_belongs_to_different_user_returns_404(
        self, api_client, save_entry, retrieve_entry
    ):
        user_1 = baker.make(User)
        entry_1 = save_entry(user_id=user_1.id)
        user_2 = baker.make(User)
        api_client.force_authenticate(user=user_2)

        response = retrieve_entry(entry_1.id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_entry_id_is_valid_returns_200(
        self, save_entry, api_client, retrieve_entry
    ):
        user = baker.make(User)
        entry = save_entry(user_id=user.id)
        api_client.force_authenticate(user=user)

        response = retrieve_entry(entry.id)

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestUpdateEntry:
    def test_if_user_is_anonymous_returns_401(self, update_entry):
        response = update_entry("a", {})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_entry_id_is_invalid_returns_404(self, authenticate, update_entry):
        authenticate()

        response = update_entry("a", {})

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_data_is_invalid_returns_400(self, api_client, save_entry, update_entry):
        user = baker.make(User)
        entry = save_entry(user_id=user.id)
        api_client.force_authenticate(user=user)

        response = update_entry(
            entry.id,
            {
                "title": "aa",
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_data_is_valid_returns_200(self, api_client, save_entry, update_entry):
        user = baker.make(User)
        entry = save_entry(user_id=user.id)
        api_client.force_authenticate(user=user)

        response = update_entry(
            entry.id,
            {
                "title": "aa",
                "username": "aa",
                "password": "aa",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "title": "aa",
            "username": "aa",
            "password": "aa",
            "notes": None,
            "url": None,
        }


@pytest.mark.django_db
class TestPartialUpdateEntry:
    def test_if_user_is_anonymous_returns_401(self, partial_update_entry):
        response = partial_update_entry("a", {})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_entry_id_is_invalid_returns_404(
        self, authenticate, partial_update_entry
    ):
        authenticate()

        response = partial_update_entry("a", {})

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_data_is_invalid_returns_400(
        self, api_client, save_entry, partial_update_entry
    ):
        user = baker.make(User)
        entry = save_entry(user_id=user.id)
        api_client.force_authenticate(user=user)

        response = partial_update_entry(
            entry.id,
            {
                "url": "a",
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_data_is_valid_returns_200(
        self, api_client, save_entry, partial_update_entry
    ):
        user = baker.make(User)
        entry = save_entry(user_id=user.id)
        api_client.force_authenticate(user=user)

        response = partial_update_entry(
            entry.id,
            {
                "title": "aa",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "aa"


@pytest.mark.django_db
class TestDeleteEntry:
    def test_if_user_is_anonymous_returns_401(self, delete_entry):
        response = delete_entry("a")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_entry_id_is_invalid_returns_404(self, authenticate, delete_entry):
        authenticate()

        response = delete_entry("a")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_entry_id_belongs_to_different_user_returns_404(
        self, api_client, save_entry, delete_entry
    ):
        user_1 = baker.make(User)
        entry_1 = save_entry(user_id=user_1.id)
        user_2 = baker.make(User)
        api_client.force_authenticate(user=user_2)

        response = delete_entry(entry_1.id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_entry_id_is_valid_returns_204(
        self, api_client, save_entry, delete_entry
    ):
        user = baker.make(User)
        entry = save_entry(user_id=user.id)
        api_client.force_authenticate(user=user)

        response = delete_entry(entry.id)

        assert response.status_code == status.HTTP_204_NO_CONTENT
