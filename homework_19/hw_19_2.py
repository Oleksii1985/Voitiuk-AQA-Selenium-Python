"""
Создать класс LocalStorage который умеет через веб драйвер сохранять и возвращать аргументы.
LocalStorage класс должен инстанцироваться в базовой страницу приложения где у вас есть экземпляр драйвера.
"""


def test_local_storage(dashboard2):
    print(dashboard2.save_and_return_local_storage())
