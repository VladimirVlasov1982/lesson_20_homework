import pytest

from service.director import DirectorService
from tests.test_service.conftest import call_method


class TestDirectorService:
    """Тестируем сервисы режиссера"""

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        # Проверяем получение одного режиссера
        director = self.director_service.get_one(1)

        assert director is not None, "Режиссер отсутствует"
        assert director.id is not None, "id режиссера отсутствует"

    def test_director_get_all(self):
        # Проверяем получение списка всех режиссеров
        directors = self.director_service.get_all()

        assert len(directors) > 0, "Список режиссеров пуст"

    def test_create(self):
        # Проверяем создание режиссера
        director_data = {
            "name": "director new"
        }
        director = self.director_service.create(director_data)

        assert director is not None, "Новый режиссер не создан"

    def test_update(self):
        # Проверяем обновление режиссера
        director_data = {
            "name": "director update"
        }
        self.director_service.update(director_data)

    def test_delete(self):
        # Проверяем удаление режиссера
        self.director_service.delete(1)

    def test_has_to_fail(self):
        with pytest.raises(Exception):
            call_method()
