class Book():
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def display_info(self):
        return f"'{self.title}' by {self.author}. ISBN: ({self.ISBN})."
    

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.\n")
    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.\n")
                return
            
    def find_book(self, book_name):
        for book in self.books:
            if book_name == book.title:
                print(f"Your book is found! {book.display_info()}\n")
                return
        print("Book not found in the library.")

    def list_books(self):
        print("Books in the library: \n")
        for book in self.books:
            print(book.display_info())
        print()

# Example usage:
library = Library()
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
library.add_book(book1)
library.add_book(book2)
library.list_books()
library.find_book("1984")
library.remove_book("1234567890")
library.list_books()

    
