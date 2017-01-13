from functions import load_contacts_from_file
from storage import add_contact, delete_contact, find_contact

filename = 'book.txt'


def add(first_name, last_name, tel_number):
    name = '{} {}'.format(first_name, last_name)
    add_contact(name, tel_number)

    print('Added contact "{} {}, {}"'.format(first_name, last_name, tel_number))


def remove(first_name, last_name):
    print(delete_contact(first_name, last_name))


def find(request):
    print(find_contact(request))


def help():
    print(
    '''
Commands:

    - add - adds a new entry in the address book
    - remove - removes the entry from the address book
    - find - is looking for an entry in the address book

Examples:

    Record addition
    > python address_book.py add John Doe +79999999999
    Added contact "John Doe, +79999999999"

    Deleting records
    > python address_book.py remove Max Payne
    Unknown contact "Max Payne"

    > python address_book.py remove John Doe
    Removed contact "John Doe, +79999999999"

    Search records
    > python address_book.py find Max
    No results for "Max"

    > python address_book.py find John
    Found for "John":
        - "John Doe, +79999999999"

    > python address_book.py find 999
    Found for "999":
        - "John Doe, +79999999999"
    ''')



