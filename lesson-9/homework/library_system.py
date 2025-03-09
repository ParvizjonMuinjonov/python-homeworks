from datetime import datetime

# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book Class
class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title.strip()
        self.author = author.strip()
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"{self.title}, {self.author}, {'Borrowed' if self.is_borrowed else 'Not borrowed'}"

# Member Class
class Member:
    def __init__(self, name):
        self.name = name.strip()
        self.max_books = 3

    def count_borrowed_books(self):
        try:
            with open("borrowed_books.txt", "r") as file:
                return sum(1 for line in file if self.name in line and "Borrowed" in line)
        except FileNotFoundError:
            return 0

# Library Class
class Library:
    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        book = Book(title, author)

        try:
            with open("books.txt", "r") as file:
                if any(f"{book.title}, {book.author}" in line for line in file):
                    print(f"Book '{book.title}' already exists.")
                    return
        except FileNotFoundError:
            pass

        with open("books.txt", "a") as file:
            file.write(f"{book}\n")
        print(f"Added book: {book}")

    def add_member(self):
        name = input("Enter member name: ").strip()
        member = Member(name)

        try:
            with open("members.txt", "r") as file:
                if any(member.name == line.strip() for line in file):
                    print(f"Member '{member.name}' already exists.")
                    return
        except FileNotFoundError:
            pass

        with open("members.txt", "a") as file:
            file.write(f"{member.name}\n")
        print(f"Added member: {member.name}")

    def borrow_book(self, book_title, member_name):
        book_found = False
        book_lines = []

        try:
            with open("books.txt", "r") as file:
                book_lines = file.readlines()
                for i, line in enumerate(book_lines):
                    parts = line.strip().split(", ")
                    if parts[0] == book_title:
                        book_found = True
                        if parts[2] == "Borrowed":
                            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed!")
                        book_lines[i] = f"{parts[0]}, {parts[1]}, Borrowed\n"
                        break
                if not book_found:
                    raise BookNotFoundException(f"Book '{book_title}' not found!")
        except FileNotFoundError:
            raise BookNotFoundException("Books file missing!")

        try:
            with open("members.txt", "r") as file:
                if member_name not in [line.strip() for line in file]:
                    raise Exception(f"Member '{member_name}' not found!")
        except FileNotFoundError:
            raise Exception("Members file missing!")

        member = Member(member_name)
        if member.count_borrowed_books() >= member.max_books:
            raise MemberLimitExceededException(f"{member_name} has reached the borrowing limit!")

        with open("books.txt", "w") as file:
            file.writelines(book_lines)

        with open("borrowed_books.txt", "a") as file:
            file.write(f"{book_title}, {member_name}, {datetime.now()}, Borrowed\n")
        print(f"{member_name} borrowed '{book_title}'")

    def return_book(self, book_title, member_name):
        borrowed_lines = []
        found = False
        try:
            with open("borrowed_books.txt", "r") as file:
                borrowed_lines = file.readlines()
                for line in borrowed_lines:
                    if book_title in line and member_name in line and "Borrowed" in line:
                        found = True
                        break
            if not found:
                print(f"{member_name} did not borrow '{book_title}'.")
                return
        except FileNotFoundError:
            print("No borrowed books found.")
            return

        with open("borrowed_books.txt", "w") as file:
            for line in borrowed_lines:
                if book_title in line and member_name in line and "Borrowed" in line:
                    with open("returned_books.txt", "a") as file2:
                        file2.write(line.replace("Borrowed", "Returned"))
                else:
                    file.write(line)

        with open("books.txt", "r") as file:
            book_lines = file.readlines()
        with open("books.txt", "w") as file:
            for line in book_lines:
                parts = line.strip().split(", ")
                if parts[0] == book_title:
                    file.write(f"{parts[0]}, {parts[1]}, Not borrowed\n")
                else:
                    file.write(line)
        print(f"{member_name} returned '{book_title}'")

    def view_available_books(self):
        try:
            with open("books.txt", "r") as file:
                books = [line.strip() for line in file if "Not borrowed" in line]
                print("Available books:")
                for book in books:
                    print(book)
        except FileNotFoundError:
            print("No books found.")

    def view_members(self):
        try:
            with open("members.txt", "r") as file:
                members = [line.strip() for line in file]
                for member_name in members:
                    print(member_name)
        except FileNotFoundError:
            print("No members found.")

if __name__ == "__main__":
    library = Library()
    library.view_available_books()
