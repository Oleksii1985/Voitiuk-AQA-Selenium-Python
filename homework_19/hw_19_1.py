"""
Создать класс Cookie который умеет через веб драйвер сохранять и возвращать куки.
Куки клас должен инстанцироваться в базовой страницу приложения где у вас есть экземпляр драйвера.
"""


def test_save_and_return_cookies(dashboard1):
    print(dashboard1.save_and_return_cookies())
