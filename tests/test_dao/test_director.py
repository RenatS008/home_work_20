from unittest.mock import MagicMock
import pytest

from application.dao.director_dao import DirectorDAO
from application.dao.model.director import Director


@pytest.fixture(autouse=True)
def d_dao():
    director_dao = DirectorDAO(None)

    director1 = Director(id=1, name="testname_1")
    director2 = Director(id=2, name="testname_2")

    director_dao.get_all = MagicMock(return_value=[director1, director2])
    director_dao.get_by_id = MagicMock(return_value=director1)
    director_dao.create = MagicMock(return_value=director1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao
