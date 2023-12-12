from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    book1 = 'Что делать, если ваш кот хочет вас убить'
    book2 = 'Гордость и предубеждение и зомби'
    book_genre_horrors = 'Ужасы'
    book_genre_detectives = 'Детективы'
    book_genre_thriller = 'Триллер'

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book(self.book2)
        collector.add_new_book(self.book1)
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # добавление книги с названием более 40 символов
    def test_add_new_book_add_books_title_more_40_characters(self):
        collector = BooksCollector()
        collector.add_new_book('Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции')
        assert len(collector.get_books_genre()) == 0

    # добавление двух одинаковых книг
    def test_add_new_book_add_books_similar_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book1)
        assert len(collector.get_books_genre()) == 1

    # добавление книги с отсутствующим жанром
    def test_set_book_genre_is_no_such_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_thriller)
        assert collector.get_book_genre(self.book1) == ''

    # вывод жанра книги по её имени.
    def test_get_book_genre_is_such_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_horrors)
        assert collector.get_book_genre(self.book1) == self.book_genre_horrors

    # вывод списка книг с определённым жанром.
    def test_get_books_with_specific_genre_books_same_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_horrors)
        collector.add_new_book(self.book2)
        collector.set_book_genre(self.book2, self.book_genre_detectives)
        assert collector.get_books_with_specific_genre(self.book_genre_horrors) == [self.book1]

    # возвращает книги, которые подходят детям
    def test_get_books_for_children_no_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_horrors)
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        assert collector.get_books_for_children() == ['Хоббит']

    # добавляет книгу в избранное. Книга должна находиться в словаре
    @pytest.mark.parametrize('new_book1', ['Что делать, если ваш кот хочет вас убить',
                                           'Гордость и предубеждение и зомби'])
    def test_add_book_in_favorites_adding_favorites(self, new_book1):
        collector = BooksCollector()
        collector.add_new_book(new_book1)
        collector.add_book_in_favorites(new_book1)
        assert collector.get_list_of_favorites_books() == [new_book1]

    # повторно добавить книгу в избранное нельзя.
    @pytest.mark.parametrize('new_book1', ['Что делать, если ваш кот хочет вас убить',
                                           'Гордость и предубеждение и зомби'])
    def test_add_book_in_favorites_if_missing(self, new_book1):
        collector = BooksCollector()
        collector.add_new_book(new_book1)
        collector.add_book_in_favorites(new_book1)
        collector.add_new_book(new_book1)
        collector.add_book_in_favorites(new_book1)
        assert collector.get_list_of_favorites_books() == [new_book1]

    # удаляет книгу из избранного. Книга должна находиться в словаре
    def test_delete_book_from_favorites_delete_favorites_if_present(self):
        collector = BooksCollector()
        collector.add_new_book(self.book2)
        collector.add_new_book(self.book1)
        collector.add_book_in_favorites(self.book2)
        collector.add_book_in_favorites(self.book1)
        collector.delete_book_from_favorites(self.book1)
        assert collector.get_list_of_favorites_books() == [self.book2]
