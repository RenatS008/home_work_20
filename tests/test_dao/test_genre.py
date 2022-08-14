from unittest.mock import MagicMock
import pytest

from application.dao.genre_dao import GenreDAO
from application.dao.model.genre import Genre


@pytest.fixture(autouse=True)
def d_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name="testgenre_1")
    genre2 = Genre(id=2, name="testgenre_2")

    genre_dao.get_all = MagicMock(return_value=[genre1, genre2])
    genre_dao.get_by_id = MagicMock(return_value=genre1)
    genre_dao.create = MagicMock(return_value=genre1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao
