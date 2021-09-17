"""
Повторить структуры проекта из лекции и организовать пэйдж обджекты
реализовать инстанцирование драйвера и его настройку в фикстуре драйвер
Описать базовые методы по клику, сенд кейсу, скролу и прочие в базовой странице
переписать существующие тесты под новую структуру
"""
from .test_fixtures import dashboard
from .test_fixtures import driver


def test_check_input_and_scroll(dashboard):
    dashboard.choose_product_list("розетки")
    dashboard.click_product()
