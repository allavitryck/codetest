class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False

    def __str__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nStatus: {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def view_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Library Books:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book.title} by {book.author}")

    def check_out_book(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            if book.check_out():
                print(f"Checked out '{book.title}' by {book.author}.")
            else:
                print(f"'{book.title}' is already checked out.")
        else:
            print("Invalid book index.")

    def return_book(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            if book.return_book():
                print(f"Returned '{book.title}' by {book.author}.")
            else:
                print(f"'{book.title}' is already available in the library.")
        else:
            print("Invalid book index.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Check Out Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            index = int(input("Enter the index of the book to check out: "))
            library.check_out_book(index)
        elif choice == "4":
            index = int(input("Enter the index of the book to return: "))
            library.return_book(index)
        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
