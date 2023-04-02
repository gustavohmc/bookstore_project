import utils.database

books = [
    {
        'name': 'Foundation',
        'author': 'Isaac Azimov',
        'read': False
    },
    {
        'name': 'Brave New World',
        'author': 'Aldous Huxley',
        'read': False
    }
]


def add_book():
    new_name = input('What is the name of the book you want to add? ')
    for book in books:
        if book['name'] == new_name:
            print('This book already exists in the collection')
            return
    new_author = input('Who is the author?')
    books.append({'name': new_name, 'author': new_author, 'read': False})
    print(f'Book {new_name} added to the list')


def list_all_books():
    for book in books:
        print(f'Title: {book["name"]}, Author: {book["author"]}, Read: {"Yed" if book["read"] else "No"}')


def mark_as_read():
    book_to_update = input('Which book should I mark as read? ')
    for book in books:
        if book['name'] == book_to_update:
            if book['read']:
                print('This book is already marked as read')
            else:
                book['read'] = True
                print(f'Book {book_to_update} was marked as read')
            return

    else:
        print(f'There is no book named {book_to_update} in the database')


def delete_book():
    book_to_delete = input('Which book would you like to delete?')
    utils.database.books = [book for book in utils.database.books if book['name'] != book_to_delete]
    print(f'Book {book_to_delete} was removed from the collection')
