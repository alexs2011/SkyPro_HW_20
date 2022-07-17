import pytest

from dao.model.genre import Genre
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert isinstance(genre, Genre)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        data = {"name": "new genre"}
        new_genre = self.genre_service.create(data)
        assert isinstance(new_genre, Genre)
        assert new_genre.id is not None

    def test_update(self):
        data = {"name": "updated name"}
        self.genre_service.update(data)

    def test_partially_update(self):
        data = {"id": 1, "name": "updated name"}
        self.genre_service.partially_update(data)

    def test_delete(self):
        self.genre_service.delete(1)
