"""
Закончить парсер для XML который я начал на занятии.
Класс Movie с помощью метода from_xml должен возвращать список объектов типа Movie
"""

from __future__ import annotations

from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(
        self,
        title: str,
        format_: str,
        year: str,
        rating: str,
        description: str,
        category: str,
    ):
        self.title = title
        self.format_ = format_
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for movie in collection.iter("movie"):
            for child in movie.findall("*"):
                movies.append(child.text)
        return movies


if __name__ == '__main__':
    movies_ = Movie.from_xml("market.xml")
    print(movies_)
