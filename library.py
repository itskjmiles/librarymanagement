from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if self.books:
            print("List of Books:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book.title} by {book.author}")
        else:
            print("No books available in the library.")
