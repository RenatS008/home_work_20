from unittest.mock import MagicMock
import pytest

from application.dao.model.movie import Movie
from application.dao.movie_dao import MovieDAO


@pytest.fixture(autouse=True)
def d_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1,
                   title="title_1",
                   description="description_1",
                   trailer="trailer_1",
                   year=2022,
                   rating=10
                   )
    movie2 = Movie(id=2,
                   title="title_2",
                   description="description_2",
                   trailer="trailer_2",
                   year=2022,
                   rating=20
                   )

    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.get_by_id = MagicMock(return_value=movie1)
    movie_dao.create = MagicMock(return_value=movie1)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
