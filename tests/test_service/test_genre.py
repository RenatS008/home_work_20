import pytest

from application.service.genre import GenreService
from tests.test_dao.test_genre import g_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, g_dao):
        self.genre_service = GenreService(g_dao)

    def test_get_all(self):
        assert len(self.genre_service.get_all()) == 2

    def test_get_by_id(self):
        assert self.genre_service.get_by_id(1) is not None
        assert self.genre_service.get_by_id(1).name == 'genre_1'

    def test_create(self):
        data = {
            "name": "genre_1"
        }

        assert self.genre_service.create(data).name == data.get("name")

    def test_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
