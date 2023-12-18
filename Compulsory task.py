import sqlite3

# Create SQLite database / connect to database
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# Create the 'books' table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')

# Insert initial data into the table
cursor.executemany('''
    INSERT INTO books (title, author, qty)
    VALUES (?, ?, ?)
''', [
    ('A Tale of Two Cities', 'Charles Dickens', 30),
    ('Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40),
    ('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    ('The Lord of the Rings', 'J.R.R Tolkien', 37),
    ('Alice in Wonderland', 'Lewis Carroll', 12)
])

# Commit the changes to the database
conn.commit()

# Get user input
def enter_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    qty = int(input("Enter the quantity of the book: "))

    # Code to enter a new book to the database
    cursor.execute('''
        INSERT INTO books (title, author, qty)
        VALUES (?, ?, ?)
    ''', (title, author, qty))
    conn.commit()
    print("Book added successfully.")

def update_book():
    book_id = int(input("Please enter the id of the book to update: "))
    new_qty = int(input("Enter the new quantity for the book: "))

    # Code to update book info
    cursor.execute('''
        UPDATE books
        SET qty = ?
        WHERE id = ?
    ''', (new_qty, book_id))
    conn.commit()
    print("Book updated successfully.")

def delete_book():
    # Get user input for book id to delete
    book_id = int(input("Enter the id of the book to delete: "))

    # Code to delete book from database
    cursor.execute('''
        DELETE FROM books
        WHERE id = ?
    ''', (book_id,))
    conn.commit()
    print("Book deleted successfully.")

def search_books():
    # Get user input for book title to search
    search_title = input("Enter the title of the book to search for: ")

    # Code to search for a book
    cursor.execute('''
        SELECT * FROM books
        WHERE title LIKE ?
    ''', ('%' + search_title + '%',))

    results = cursor.fetchall()

    if results:
        print("Search results:")
        for row in results:
            print(row)
        else: 
            print("Book not found.")

# Main program
while True:
    print("\Menu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

    choice = input("Please enter your choice: ")

    if choice == '1':
        enter_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()





