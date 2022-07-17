import pytest

from dao.model.movie import Movie
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert isinstance(movie, Movie)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        data = {
            "title": 'new movie',
            "description": "description",
            "trailer": 'trailer',
            "year": 2020,
            "rating": 4,
            "genre_id": 3,
            "director_id": 3
        }
        new_movie = self.movie_service.create(data)
        assert isinstance(new_movie, Movie)
        assert new_movie.id is not None
        assert new_movie.title == 'movie_3'

    def test_update(self):
        data = {
            "title": 'new movie',
            "description": "description",
            "trailer": 'trailer',
            "year": 2019,
            "rating": 3,
            "genre_id": 1,
            "director_id": 2
        }
        self.movie_service.update(data)

    def test_partially_update(self):
        data = {"id": 1, "title": "updated name"}
        self.movie_service.partially_update(data)

    def test_delete(self):
        self.movie_service.delete(1)
