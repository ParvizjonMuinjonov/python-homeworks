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
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"{self.title}, {self.author}, {'Borrowed' if self.is_borrowed else 'Not borrowed'}"

# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.max_books = 3

    def __str__(self):
        return f"{self.name}"

    def count_borrowed_books(self):
        try:
            with open("borrowed_books.txt", "r") as file:
                lines = file.readlines()
                return sum(1 for line in lines if self.name in line and "Borrowed" in line)
        except FileNotFoundError:
            return 0

# Library Class
class Library:
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = Book(title, author)

        # Check if book already exists to avoid duplicates
        try:
            with open("books.txt", "r") as file:
                if f"{book.title}, {book.author}" in file.read():
                    print(f"Book '{book.title}' by {book.author} already exists, skipping.")
                    return
        except FileNotFoundError:
            pass  # File doesn’t exist yet, so proceed to add

        with open("books.txt", "a") as file:
            file.write(f"{book}\n")
        print(f"Added book: {book}")

    def add_member(self):
        name = input("Enter member name: ")
        member = Member(name)

        # Check for duplicates
        try:
            with open("members.txt", "r") as file:
                if member.name in file.read():
                    print(f"Member '{member.name}' already exists, skipping.")
                    return
        except FileNotFoundError:
            pass

        with open("members.txt", "a") as file:
            file.write(f"{member.name}\n")
        print(f"Added member: {member}")

    def borrow_book(self, book_title, member_name):
        # Check if book exists and its status
        book_found = False
        book_lines = []
        try:
            with open("books.txt", "r") as file:
                book_lines = file.readlines()
                for i, line in enumerate(book_lines):
                    if book_title in line:
                        book_found = True
                        if "Borrowed" in line:
                            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed!")
                        book_lines[i] = f"{book_title}, {line.split(', ')[1]}, Borrowed\n"
                        break
                if not book_found:
                    raise BookNotFoundException(f"Book '{book_title}' not found in the library!")
        except FileNotFoundError:
            raise BookNotFoundException(f"Book '{book_title}' not found (books.txt missing)!")

        # Check if member exists
        member_found = False
        try:
            with open("members.txt", "r") as file:
                if member_name in [line.strip() for line in file]:
                    member_found = True
            if not member_found:
                raise Exception(f"Member '{member_name}' not found!")
        except FileNotFoundError:
            raise Exception(f"Member '{member_name}' not found (members.txt missing)!")

        # Check member's borrowing limit
        member = Member(member_name)
        if member.count_borrowed_books() >= member.max_books:
            raise MemberLimitExceededException(f"{member_name} has reached the borrowing limit of {member.max_books} books!")

        # Update books.txt
        with open("books.txt", "w") as file:
            file.writelines(book_lines)

        # Record borrowing
        with open("borrowed_books.txt", "a") as file:
            date = datetime.now()
            file.write(f"{book_title}, {member_name}, {date}, Borrowed\n")
        print(f"{member_name} borrowed '{book_title}' on {date}")

    def return_book(self, book_title, member_name):
        # Check if the book is borrowed by this member
        found = False
        borrowed_lines = []
        try:
            with open("borrowed_books.txt", "r") as file:
                borrowed_lines = file.readlines()
                for line in borrowed_lines:
                    if book_title in line and member_name in line and "Borrowed" in line:
                        found = True
                        break
            if not found:
                print(f"{member_name} does not have '{book_title}' borrowed.")
                return
        except FileNotFoundError:
            print(f"No borrowed books record found.")
            return

        # Update borrowed_books.txt
        with open("borrowed_books.txt", "w") as file:
            for line in borrowed_lines:
                if book_title in line and member_name in line and "Borrowed" in line:
                    with open("returned_books.txt", "a") as file2:
                        file2.write(line.replace("Borrowed", "Returned"))
                else:
                    file.write(line)

        # Update books.txt to mark as not borrowed
        try:
            with open("books.txt", "r") as file:
                book_lines = file.readlines()
            with open("books.txt", "w") as file:
                for line in book_lines:
                    if book_title in line:
                        file.write(f"{book_title}, {line.split(', ')[1]}, Not borrowed\n")
                    else:
                        file.write(line)
        except FileNotFoundError:
            print("Books file not found!")
            return

        print(f"{member_name} returned '{book_title}' on {datetime.now()}")

    def view_available_books(self):
        try:
            with open("books.txt", "r") as file:
                lines = file.readlines()
                available = [line.strip() for line in lines if "Not borrowed" in line]
                if available:
                    print("Available books:")
                    for book in available:
                        print(book)
                else:
                    print("No books available.")
        except FileNotFoundError:
            print("No books file found. Please add books first.")

    def view_members(self):
        try:
            with open("members.txt", "r") as file:
                members = [line.strip() for line in file]
                if members:
                    print("Library members:")
                    for member_name in members:
                        member = Member(member_name)
                        borrowed_count = member.count_borrowed_books()
                        print(f"{member_name} (Borrowed: {borrowed_count}/{member.max_books})")
                        if borrowed_count > 0:
                            print("  Borrowed books:")
                            with open("borrowed_books.txt", "r") as file2:
                                for line in file2:
                                    if member_name in line and "Borrowed" in line:
                                        print(f"    {line.strip()}")
                else:
                    print("No members in the library.")
        except FileNotFoundError:
            print("No members file found. Please add members first.")

def main():
    library = Library()

    # Create empty files if they don’t exist
    for filename in ["books.txt", "members.txt", "borrowed_books.txt", "returned_books.txt"]:
        try:
            with open(filename, "a"):
                pass  # Just create the file if it doesn’t exist
        except Exception as e:
            print(f"Error creating {filename}: {e}")

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Add a member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View available books")
        print("6. View members")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice == 1:
                library.add_book()

            elif choice == 2:
                library.add_member()

            elif choice == 3:
                member_name = input("Enter member name: ")
                book_title = input("Enter book title to borrow: ")
                library.borrow_book(book_title, member_name)

            elif choice == 4:
                member_name = input("Enter member name: ")
                book_title = input("Enter book title to return: ")
                library.return_book(book_title, member_name)

            elif choice == 5:
                library.view_available_books()

            elif choice == 6:
                library.view_members()

            elif choice == 7:
                print("Exiting Library System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError:
            print("Please enter a valid number.")
        except BookNotFoundException as e:
            print(f"Error: {e}")
        except BookAlreadyBorrowedException as e:
            print(f"Error: {e}")
        except MemberLimitExceededException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()