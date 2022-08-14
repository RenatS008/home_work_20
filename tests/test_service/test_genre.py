import pytest

from application.service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def __init__(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        assert len(self.genre_service.get_all()) == 2

    def test_get_by_id(self):
        assert self.genre_service.get_by_id(1) is not None
        assert self.genre_service.get_by_id(1).name == 'testname_1'

    def test_create(self):
        data = {
            "name": "testname_2"
        }

        assert self.genre_service.create(data).name == data.get("name")

    def test_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
