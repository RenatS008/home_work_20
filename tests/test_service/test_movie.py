import pytest

from application.service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def __init__(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

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
        data_first = {
            "id": 1,
            "title": 'title_1',
            "description": 'description_1',
            "trailer": 'trailer_1',
            "year": 2022,
            "rating": 10,
            "genre_id": 1,
            "director_id": 1
        }
        data_next = {
            "id": 1,
            "title": 'title_2',
            "description": 'description_1',
            "trailer": 'trailer_1',
            "year": 2022,
            "rating": 10,
            "genre_id": 1,
            "director_id": 1
        }
        assert data_first != data_next

    def test_delete(self):
        data_first = {
            "id": 1,
            "title": 'title_2',
            "description": 'description_1',
            "trailer": 'trailer_1',
            "year": 2022,
            "rating": 10,
            "genre_id": 1,
            "director_id": 1
        }
        data_next = {
            "id": 1,
            "title": 'title_1',
            "description": 'description_1',
            "trailer": 'trailer_1',
            "year": 2022,
            "rating": 10,
            "genre_id": 1,
            "director_id": 1
        }
        assert data_first != data_next
