from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='director_1')
    d2 = Director(id=2, name='director_2')
    d3 = Director(id=3, name='director_3')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])

    director_dao.create = MagicMock(return_value=d3)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='genre_1')
    g2 = Genre(id=2, name='genre_2')
    g3 = Genre(id=3, name='genre_3')

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])

    genre_dao.create = MagicMock(return_value=g3)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(
        id=1,
        title='movie_1',
        description="description_1",
        trailer='trailer_1',
        year=2017,
        rating=4,
        genre_id=4,
        director_id=3
    )
    m2 = Movie(
        id=2,
        title='movie_2',
        description="description_2",
        trailer='trailer_2',
        year=2018,
        rating=6,
        genre_id=5,
        director_id=6
    )
    m3 = Movie(
        id=3,
        title='movie_3',
        description="description_3",
        trailer='trailer_3',
        year=2019,
        rating=5,
        genre_id=2,
        director_id=3
    )

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])

    movie_dao.create = MagicMock(return_value=m3)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
