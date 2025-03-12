import sqlite3
import random

# Corrected table creation
table = """
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
"""

# Book data
insert_data = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
    ("Pride and Prejudice", "Jane Austen", 1813, "Classic"),
    ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
    ("Brave New World", "Aldous Huxley", 1932, "Dystopian"),
    ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic"),
]

# Setup database
def setup_database():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute(table)
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM Books")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO Books VALUES(?, ?, ?, ?)", insert_data)
        connection.commit()

    return connection, cursor  

conn, cursor = setup_database()

# Insert new data
def new_data(cursor, connection):
    title = input("Enter title: ")
    author = input("Enter author: ")
    year_published = int(input("Enter year published: "))
    genre = input("Enter genre: ")
    cursor.execute("INSERT INTO Books VALUES(?, ?, ?, ?)", (title, author, year_published, genre))
    connection.commit()
    print("Data inserted successfully")

# Update year data
def update_data(cursor, connection):
    new_year = int(input("Enter new year: ")) 
    old_year = int(input("Enter old year: "))  
    cursor.execute("UPDATE Books SET Year_Published = ? WHERE Year_Published = ?", (new_year, old_year))
    connection.commit()
    print("Data updated successfully")

# Display data
def display_data(cursor):
    genre_list = ["Fiction", "Dystopian", "Classic"]
    print(f"Choose genre: {genre_list}") 
    choose_genre = input("Enter genre: ")

    if choose_genre not in genre_list:
        print("Invalid genre")
        return

    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", (choose_genre,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No records found.")

# Remove data
def remove_data(cursor, connection):
    try:
        chosen_year = int(input("Enter year published: "))
        cursor.execute("DELETE FROM Books WHERE Year_Published < ?", (chosen_year,))
        connection.commit()
        print("Data removed successfully")
    except ValueError:
        print("Invalid year published")

# Add new column
def add_column(cursor, connection):
    column_name = input("Enter column name: ")
    cursor.execute(f"ALTER TABLE Books ADD COLUMN {column_name} TEXT")
    connection.commit()
    print("Column added successfully")

    rating = round(random.uniform(3.6, 5.0), 1)  
    cursor.execute(f"UPDATE Books SET {column_name} = ?", (rating,))
    connection.commit()

# Sort data
def sort_data(cursor):
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published DESC") 
    results = cursor.fetchall()
    for row in results:
        print(row)

# Main menu
def main():
    while True:
        print("""
            1. Insert new book to the library
            2. Update year in the library  
            3. Display the title and the author of certain genre books
            4. Remove all books published before a certain year
            5. Add new column to the table
            6. Sort books by published year
            7. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            new_data(cursor, conn)
        elif choice == "2":
            update_data(cursor, conn)
        elif choice == "3":
            display_data(cursor)
        elif choice == "4":
            remove_data(cursor, conn)
        elif choice == "5":
            add_column(cursor, conn)  
        elif choice == "6":
            sort_data(cursor)  
        elif choice == "7":
            conn.close()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
