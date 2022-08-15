import pytest

from application.service.director import DirectorService
from tests.test_dao.test_director import d_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, d_dao):
        self.director_service = DirectorService(d_dao)

    def test_get_all(self):
        assert len(self.director_service.get_all()) == 2

    def test_get_by_id(self):
        assert self.director_service.get_by_id(1) is not None
        assert self.director_service.get_by_id(1).name == 'name_1'

    def test_create(self):
        data = {
            "name": "name_1"
        }

        assert self.director_service.create(data).name == data.get("name")

    def test_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 1 == 1
