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
            database.add_book()
        elif user_input == 'l':
            database.list_all_books()
        elif user_input == 'r':
            database.mark_as_read()
        elif user_input == 'd':
            database.delete_book()

        user_input = input(USER_CHOICE)

menu()
