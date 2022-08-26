import pytest
from service.movie import MovieService
from tests.test_service.conftest import call_method


class TestMovieService:
    """Тестируем сервисы фильмов"""

    @pytest.fixture(autouse=True)
    def user_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_det_one(self):
        # Проверяем получение одного фильма
        movie = self.movie_service.get_one(1)

        assert movie is not None, "Фильм отсутствует"
        assert movie.id is not None, "id отсутствует"

    def test_get_all(self):
        # Проверяем получение списка всех фильмов
        movies = self.movie_service.get_all()

        assert len(movies) > 0, "Список фильмов пуст"

    def test_create(self):
        # Проверяем создание фильма
        movie_data = {
            "title": "movie new",
            "description": "description new",
            "trailer": "trailer new",
            "year": 2012,
            "rating": 8.4,
            "genre_id": 17,
            "director_id": 2,
        }
        movie = self.movie_service.create(movie_data)

        assert movie.id is not None, "Фильм не создался"

    def test_update(self):
        # Проверяем обновление фильма
        movie_data = {
            "title": "movie update",
            "description": "description update",
            "trailer": "trailer update",
            "year": 2012,
            "rating": 8.4,
            "genre_id": 17,
            "director_id": 2,
        }
        self.movie_service.update(movie_data)

    def test_delete(self):
        # Проверяем удаление фильма
        self.movie_service.delete(1)

    def test_has_to_fail(self):
        with pytest.raises(Exception):
            call_method()
