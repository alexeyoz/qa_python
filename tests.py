from main import BooksCollector
import pytest


# TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:
    book1 = 'Что делать, если ваш кот хочет вас убить'
    book2 = 'Гордость и предубеждение и зомби'
    book_genre_horrors = 'Ужасы'
    book_genre_detectives = 'Детективы'
    book_genre_thriller = 'Триллер'

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

    '''
    1. добавление книг вне границ условия: 0, 41, 42 символа
    '''
    @pytest.mark.parametrize('new_book1', ['',
                                           '01234567890123456789012345678901234567891',
                                           '012345678901234567890123456789012345678912'])
    def test_add_new_book_add_books_names_are_not_allowed(self, new_book1):
        collector = BooksCollector()
        collector.add_new_book(new_book1)
        assert len(collector.get_books_genre()) == 0

    '''
    2. добавление книг в границах условия: 1, 2, 39, 40 символов
    '''
    @pytest.mark.parametrize('new_book1', ['1',
                                           '12',
                                           '012345678901234567890123456789012345678',
                                           '0123456789012345678901234567890123456789'])
    def test_add_new_book_add_books_acceptable_names(self, new_book1):
        collector = BooksCollector()
        collector.add_new_book(new_book1)
        assert len(collector.get_books_genre()) == 1

    # 3. добавление двух одинаковых книг
    def test_add_new_book_add_books_similar_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book1)
        assert len(collector.get_books_genre()) == 1

    # 4. добавление книги с отсутствующим жанром
    def test_set_book_genre_is_no_such_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_thriller)
        assert collector.get_book_genre(self.book1) == ''

    # 5. вывод жанра книги по её имени
    def test_get_book_genre_is_such_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_horrors)
        assert collector.get_book_genre(self.book1) == self.book_genre_horrors

    # 6. вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre_books_same_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_horrors)
        collector.add_new_book(self.book2)
        collector.set_book_genre(self.book2, self.book_genre_detectives)
        assert collector.get_books_with_specific_genre(self.book_genre_horrors) == [self.book1]

    # 7. возвращает книги, которые подходят детям
    def test_get_books_for_children_no_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, self.book_genre_horrors)
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        assert collector.get_books_for_children() == ['Хоббит']

    # 8. добавляет книгу в избранное
    def test_add_book_in_favorites_adding_favorites(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_book_in_favorites(self.book1)
        assert collector.get_list_of_favorites_books() == [self.book1]

    # 9. повторно добавить книгу в избранное нельзя
    def test_add_book_in_favorites_if_missing(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_book_in_favorites(self.book1)
        collector.add_new_book(self.book1)
        collector.add_book_in_favorites(self.book1)
        assert collector.get_list_of_favorites_books() == [self.book1]

    # 10. удаляет книгу из избранного. Книга должна находиться в словаре
    def test_delete_book_from_favorites_delete_favorites_if_present(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_book_in_favorites(self.book1)
        collector.delete_book_from_favorites(self.book1)
        assert len(collector.get_list_of_favorites_books()) == 0
