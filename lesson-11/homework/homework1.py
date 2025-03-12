import sqlite3

# SQL Queries
table = "CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, Age INT)"

insert_data = [
    ('Jean-Baptiste Zorg', 'Human', 122),  
    ('Korben Dallas', 'Human', 100),  
    ('Jadzia Dax', 'Trill', 300),  
    ('Benjamin Sisko', 'Human', 40),  
    ('Kira Nerys', 'Bajoran', 29),  
    ('Julian Bashir', 'Human', 34),  
    ('Ezri Dax', 'Trill', 28),  
    ('Ro Laren', 'Bajoran', 33),  
    ('William Riker', 'Human', 45),  
    ('Deanna Troi', 'Human', 42),  
    ('Odo', 'Bajoran', 37),  
    ('Curzon Dax', 'Trill', 310),  
    ('Miles O’Brien', 'Human', 50),  
    ('Toran', 'Bajoran', 31),  
    ('Luther Sloan', 'Human', 48),  
    ('Verad', 'Trill', 290),  
    ('Keiko O’Brien', 'Human', 41),  
    ('Leeta', 'Bajoran', 30),  
    ('Emony Dax', 'Trill', 280),  
    ('Kasidy Yates', 'Human', 39)  
]

def setup_database():
    """Creates the database and table if they don't exist."""
    connection = sqlite3.connect("roster.db")
    cursor = connection.cursor()
    cursor.execute(table)
    connection.commit()

    # Insert data only if the table is empty
    cursor.execute("SELECT COUNT(*) FROM Roster")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?)", insert_data)
        connection.commit()
    
    return connection, cursor

def new_data(cursor, connection):
    name = input("Enter name: ")
    species = input("Enter species: ")
    age = int(input("Enter age: "))
    cursor.execute("INSERT INTO Roster VALUES(?, ?, ?)", (name, species, age))
    connection.commit()
    print("Data inserted successfully")

def update_data(cursor, connection):
    new_name = input("Enter new name: ")
    old_name = input("Enter old name: ")
    cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", (new_name, old_name))
    connection.commit()
    print("Data updated successfully")

def display_data(cursor):
    species_list = ["Human", "Trill", "Bajoran"]
    print(f"Choose species: {species_list}")
    choose_species = input("Enter species: ")
    
    if choose_species not in species_list:
        print("Invalid species")
        return
    
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", (choose_species,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No records found.")

def remove_data(cursor, connection):
    try:
        chosen_age = int(input("Enter age: "))
        cursor.execute("DELETE FROM Roster WHERE Age = ?", (chosen_age,))
        connection.commit()
        print("Data removed successfully")
    except ValueError:
        print("Invalid age")

def add_column(cursor, connection):
    coulumn_name = input("Enter column name: ")
    cursor.execute(f"ALTER TABLE Roster ADD COLUMN {coulumn_name} TEXT")
    connection.commit()
    print("Column added successfully")
    fixed_value = input("Enter fixed value: ")
    cursor.execute(f"UPDATE Roster SET {coulumn_name} = ?", (fixed_value,))
    connection.commit()
    print("Fixed value added successfully")

def sort_data(cursor):
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)

# Setup database and get cursor
conn, cursor = setup_database()

while True:
    print("""
          1. Insert new data to the table
          2. Update name in the table  
          3. Display name and age of certain species
          4. Remove all characters with a certain age
          5. Add new column to the table
          6. Sort characters by age
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
