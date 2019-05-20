from Book import Book

class Bookshelf(object):
    def __init__(self):
        self.book_list = []
    
    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)

    def favouriteAuthor(self):
        counter = {}
        for book in self.book_list:
            if book.author in counter:
                counter[book.author] += 1
            else:
                counter[book.author] = 1
            
        self.most_favourite = sorted(counter, key = counter.get, reverse = True)
        return self.most_favourite[0]
    
    def earliest_published(self):
        self.earliest_year = self.book_list[0].year
        for i in range(len(self.book_list)):
            if self.book_list[i].year < self.earliest_year:
                self.earliest_year = self.book_list[i].year
        return self.earliest_year

    def latest_publised(self):
        self.latest_year = self.book_list[0].year
        for i in range(len(self.book_list)):
            if self.book_list[i].year > self.latest_year:
                self.latest_year = self.book_list[i].year
        return self.latest_year

    def toString(self):
        return f"There are {len(self.book_list)} books in the book shelf\nThe ealiest book publised in {self.earliest_year}\nThe latest book published in {self.latest_year}"