from menu import Menu
from library import Library
from book import Book

def main():
    library = Library()

    while True:
        Menu.main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            borrow_book(library)
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book: ")

    book = Book(title, author, isbn, genre, publication_date)
    library.add_book(book)

def borrow_book(library):
    pass

if __name__ == "__main__":
    main()
