import json

class LibraryManager:
    def __init__(self):
        self.books = []  # List to store books
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
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'

        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read_status
        }

        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        book_found = False

        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully!")
                book_found = True
                break

        if not book_found:
            print(f"Book with title '{title}' not found!")

    def search_book(self):
        print("Search by:")
        print("1. Title")
        print("2. Author")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title: ")
            self.search_by_title(title)
        elif choice == '2':
            author = input("Enter the author: ")
            self.search_by_author(author)
        else:
            print("Invalid choice!")

    def search_by_title(self, title):
        matching_books = [book for book in self.books if title.lower() in book['title'].lower()]
        self.display_books(matching_books)

    def search_by_author(self, author):
        matching_books = [book for book in self.books if author.lower() in book['author'].lower()]
        self.display_books(matching_books)

    def display_books(self, books=None):
        if books is None:
            books = self.books
        if len(books) == 0:
            print("No books found!")
        else:
            print("Matching Books:")
            for i, book in enumerate(books, start=1):
                read_status = "Read" if book['read'] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

    def display_statistics(self):
        total_books = len(self.books)
        if total_books == 0:
            print("No books in the library!")
        else:
            read_books = sum(1 for book in self.books if book['read'])
            read_percentage = (read_books / total_books) * 100
            print(f"Total books: {total_books}")
            print(f"Percentage read: {read_percentage:.2f}%")

    def load_library(self):
        try:
            with open("library.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []

    def save_library(self):
        with open("library.json", "w") as file:
            json.dump(self.books, file)
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
