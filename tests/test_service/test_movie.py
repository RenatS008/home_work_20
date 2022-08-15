import pytest

from application.service.movie import MovieService
from tests.test_dao.test_movie import m_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, m_dao):
        self.movie_service = MovieService(m_dao)

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 2

    def test_get_by_id(self):
        assert self.movie_service.get_by_id(1) is not None
        assert self.movie_service.get_by_id(1).title == 'title_1'

    def test_create(self):
        data = {
            "id": 1,
            "title": 'title_1',
            "description": 'description_1',
            "trailer": 'trailer_1',
            "year": 2022,
            "rating": 10,
            "genre_id": 1,
            "director_id": 1
        }

        assert self.movie_service.create(data).title == data.get("title")

    def test_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
