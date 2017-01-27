from app.models import Contact
from app.storage import SqlStorage
from app.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE



storage = SqlStorage(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)

def add(first_name, last_name, tel_number):
    name = '{} {}'.format(first_name, last_name)
    contact = Contact(name, tel_number)
    result = storage.add_contact(contact)
    if result:
        print('Added contact "{}, {}"'.format(contact.name, contact.phone))
    else:
        print('Error!')


def remove(first_name, last_name):
    name = '{} {}'.format(first_name, last_name)
    result = storage.find_before_remove_contacts(first_name, last_name)
    if len(result) == 0:
        print('Unknown contact "{}"'.format(name))
    else:
        storage.remove_contact(result[0])
        print('Removed contact "{}, {}"'.format(result[0].name, result[0].phone))


def find(request):
    results = storage.find_contacts(request)
    if len(results) == 0:
        print('No results for "{}"'.format(request))
    else:
        for contact in results:
            print('Found for "{}":'.format(request))
            print('\t- "{}, {}"'.format(contact.name, contact.phone))


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

