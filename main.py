class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Not available"

        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.book = []

    def add_book(self,book):
        self.book.append(book)
        print(f"Book '{book.title}' added!")

    def show_book(self):
        print("\nLibrary Books:")
        for book in self.book:
            print(book)

    def borrow_book(self,title):
        for book in self.book:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You borrowed {title}")
                return
        print("Book not available")

    def return_book(self,title):
        for book in self.book:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"You returned {title}")
                return
        print("Invalid return")


library = Library()

while True:
    print("\n1. Add Book\n2. Show Books\n3. Borrow Book\n4. Return Book\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        library.add_book(Book(title, author))

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
