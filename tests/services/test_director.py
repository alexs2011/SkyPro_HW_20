import pytest

from dao.model.director import Director
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert isinstance(director, Director)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        data = {"name": "new director"}
        new_director = self.director_service.create(data)
        assert isinstance(new_director, Director)
        assert new_director.id is not None

    def test_update(self):
        data = {"name": "new name"}
        self.director_service.update(data)

    def test_partially_update(self):
        data = {"id": 1, "name": "new name"}
        self.director_service.partially_update(data)

    def test_delete(self):
        self.director_service.delete(1)
