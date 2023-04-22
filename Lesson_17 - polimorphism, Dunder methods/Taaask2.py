class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}, {self.books}'

    def __repr__(self):
        return str(self)

class Library:
    def __init__(self, name, books: list, authors: list):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, book_name: str, year: int, author: Author):
        self.book_name = book_name
        self.year = year
        self.author = author
        author.books.append(self.book_name)
        self.book = {'name': self.book_name, 'year': self.year, 'author': self.author}
        self.books.append(self.book)
        self.authors.append(self.author)
        return Book(self.book_name, self.year, self.author)

    def group_by_author(self, author):
        book_list = []
        for book in self.books:
            if book['author'] == author.name:
                book_list.append(book)
        return book_list

    def group_by_year(self, year: int):
        book_list = []
        for book in self.books:
            if book['year'] == year:
                book_list.append(book)
        return book_list

    def __str__(self):
        return f'Library name: {self.name}, available books: {self.books}, authors: {self.authors}'

    def __repr__(self):
        return str(self)

class Book:
    amount_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.amount_of_books += 1
        self.the_book = {'name': self.name, 'year': self.year, 'author': self.author}

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author}'

    def __repr__(self):
        return str(self)


library_1 = Library('First library', [], [])
author_1 = Author('Ayn Rand', 'USA', '02.02.1905', [])
author_2 = Author('Robert Kiyosaki', 'USA', '08.04.1947', [])
book_1 = Book('Rich dad, poor dad', 1997, author_2)
book_2 = Book('Why We Want You to Be Rich: Two Men, One Message', 2006, author_2)
library_1.new_book("Rich dad, poor dad", 1997, author_2)
library_1.new_book("Atlas Shrugged", 1957, author_1)
library_1.new_book("Atlas Shrugged", 1997, author_1)


print(library_1.books)
print(author_2.books)
# print(library_1.group_by_year(1860))
# print(library_1.group_by_author(author_1))
# print(Book.amount_of_books)
# print(library_1)
# print(repr(library_1))
# print(repr(book_1))