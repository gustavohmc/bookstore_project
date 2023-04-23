from utils import database

USER_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_mark_as_read()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('What is the name of the book? ')
    author = input('Who is the author? ')
    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'Read' if book['read'] else 'Not read'
        print(f"{book['name']} by {book['author']}, {read}")


def prompt_mark_as_read():
    book = input('Which book do you want to mark as read? ')
    database.mark_as_read(book)


def prompt_delete_book():
    book = input('Which book do you want to delete? ')
    database.delete_book(book)


database.create_book_table()
menu()
