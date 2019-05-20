from Book import Book
from Bookshelf import Bookshelf

bookshelf = Bookshelf()
book = Book("Zilan", "Hello World!", 2017)
bookshelf.add_book(book)
bookshelf.add_book(Book("Zilan", "Hello World!", 1894))
bookshelf.add_book(Book("Tony", "Hello World!", 2019))
bookshelf.remove_book(book)
print(book.toString())
print(bookshelf.favouriteAuthor())
print(bookshelf.earliest_published())
print(bookshelf.latest_publised())
print(bookshelf.toString())