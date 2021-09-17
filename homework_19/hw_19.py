"""
1. Создать класс Cookie который умеет через веб драйвер сохранять и возвращать куки.
Куки клас должен инстанцироваться в базовой страницу приложения где у вас есть экземпляр драйвера.
"""


def test_save_and_return_cookies(dashboard):
    print(dashboard.save_and_return_cookies())


"""
2. Создать класс LocalStorage который умеет через веб драйвер сохранять и возвращать аргументы.
LocalStorage класс должен инстанцироваться в базовой страницу приложения где у вас есть экземпляр драйвера.
"""


def test_local_storage(dashboard):
    print(dashboard.save_and_return_local_storage())
