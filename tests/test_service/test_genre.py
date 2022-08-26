import pytest

from service.genre import GenreService
from tests.test_service.conftest import call_method


class TestGenreService:
    """Тестируем сервисы жанров"""

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        # Проверяем получение одного жанра
        genre = self.genre_service.get_one(1)

        assert genre is not None, "Жанр отсутствует"
        assert genre.id is not None, "id жанра отсутствует"

    def test_get_all(self):
        # Проверяем получение списка всех жанров
        genres = self.genre_service.get_all()

        assert len(genres) > 0, "Список жанров пуст"

    def test_create(self):
        # Проверяяем создание жанра
        genre_data = {
            "name": "new genre"
        }
        genre = self.genre_service.create(genre_data)

        assert genre is not None, "Новый жанр не создан"

    def test_update(self):
        # Проверяем обновление жанра
        genre_data = {
            "name": "genre update"
        }
        self.genre_service.update(genre_data)

    def test_delete(self):
        # Проверяем удаление жанра
        self.genre_service.delete(1)

    def test_has_to_fail(self):
        # Обрабатываем падение или исключения наших функций
        with pytest.raises(Exception):
            call_method()
