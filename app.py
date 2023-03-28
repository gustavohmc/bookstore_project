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
            add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            mark_as_read()
        elif user_input == 'd':
            delete_book()
        elif user_input == 'q':
            exit()
        menu()


def add_book():
    pass


def list_all_books():
    pass


def mark_as_read():
    book_to_update = input('Which book should I mark as read? ')
    for book in database.books:
        if book['name'] == book_to_update:
            book['read'] = True
            print(f'Book {book_to_update} was marked as read')
            menu()
    print(f'There is no book named {book_to_update} in the database')
    menu()


def delete_book():
    pass


menu()
