import json

books_file = './utils/books.json'


def add_book():
    new_name = input('What is the name of the book you want to add? ')
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        for line in lines:
            if line[0] == new_name:
                print(f'This book is already in the collection')
                return
    new_author = input('Who is the author?')
    with open(books_file, 'a') as file:
        file.write(f'{new_name},{new_author},"No"\n')


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def list_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    books = [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]
    for book in books:
        print(f'Title: {book["name"]}, Author: {book["author"]}, Read: {book["read"]}')


def mark_as_read():
    book_to_update = input('Which book should I mark as read? ')
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    books = [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

    for book in books:
        if book['name'] == book_to_update:
            book['read'] = 'Yes'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']}, {book['read']}\n")


def delete_book():
    book_to_delete = input('Which book would you like to delete?')
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    books = [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

    for book in books:
        if book['name'] == book_to_delete:
            books.remove(book)
            print(f'{book_to_delete} was removed from the collection')
            _save_all_books(books)
