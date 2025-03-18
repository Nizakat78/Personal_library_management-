import os

class LibraryManager:
    def __init__(self):
        self.books = []  # List to store books
        self.library_file = "library.txt"
        self.load_library()

    def display_menu(self):
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        return choice

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the publication year: ")
        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'

        book = f"{title},{author},{year},{genre},{'Read' if read_status else 'Unread'}"
        self.books.append(book)
        print("Book added successfully!")
        self.save_library()

    def remove_book(self):
        title = input("Enter the title of the book to remove: ").strip().lower()
        updated_books = [book for book in self.books if not book.lower().startswith(title + ",")]
        
        if len(updated_books) == len(self.books):
            print(f"Book with title '{title}' not found!")
        else:
            self.books = updated_books
            self.save_library()
            print(f"Book '{title}' removed successfully!")

    def search_book(self):
        print("Search by:")
        print("1. Title")
        print("2. Author")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title: ").strip().lower()
            matching_books = [book for book in self.books if title in book.split(',')[0].lower()]
        elif choice == '2':
            author = input("Enter the author: ").strip().lower()
            matching_books = [book for book in self.books if author in book.split(',')[1].lower()]
        else:
            print("Invalid choice!")
            return

        self.display_books(matching_books)

    def display_books(self, books=None):
        if books is None:
            books = self.books

        if not books:
            print("No books found!")
        else:
            print("\nMatching Books:")
            for i, book in enumerate(books, start=1):
                title, author, year, genre, read_status = book.split(',')
                print(f"{i}. {title} by {author} ({year}) - {genre} - {read_status}")

    def display_statistics(self):
        total_books = len(self.books)
        if total_books == 0:
            print("No books in the library!")
            return

        read_books = sum(1 for book in self.books if book.endswith("Read"))
        read_percentage = (read_books / total_books) * 100

        print(f"Total books: {total_books}")
        print(f"Percentage read: {read_percentage:.2f}%")

    def load_library(self):
        if os.path.exists(self.library_file):
            with open(self.library_file, "r") as file:
                self.books = [line.strip() for line in file.readlines()]
        else:
            self.books = []

    def save_library(self):
        with open(self.library_file, "w") as file:
            file.write("\n".join(self.books))
        print("Library saved to file.")

    def run(self):
        while True:
            choice = self.display_menu()

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                self.save_library()
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    manager = LibraryManager()
    manager.run()
