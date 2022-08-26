from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture
def movie_dao():
    # Фикстура с моком для MovieDAO
    movie_dao = MovieDAO(None)

    movie_1 = Movie(
        id=1,
        title="title 1",
        description="description 1",
        trailer="trailer 1",
        year=2021,
        rating=8.6,
        genre_id=17,
        director_id=1,
    )
    movie_2 = Movie(
        id=2,
        title="movie 2",
        description="description 2",
        trailer="trailer 2",
        year=2015,
        rating=7.8,
        genre_id=4,
        director_id=2,
    )
    movie_3 = Movie(
        id=3,
        title="movie 3",
        description="description 3",
        trailer="trailer 3",
        year=1978,
        rating=6.0,
        genre_id=17,
        director_id=3,
    )

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


@pytest.fixture
def director_dao():
    # Фикстура с моком для DirectorDAO
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="director 1")
    director_2 = Director(id=2, name="director 2")
    director_3 = Director(id=3, name="director 3")

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    # Фикстура с моком для GenreDAO
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="genre 1")
    genre_2 = Genre(id=2, name="genre 2")
    genre_3 = Genre(id=3, name="genre 3")

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=4))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


def call_method():
    # Обработка исключений
    raise Exception()
