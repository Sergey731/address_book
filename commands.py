from storage import add_contact, delete_contact, find_contact


def add(first_name, last_name, tel_number):
    name = '{} {}'.format(first_name, last_name)
    result = add_contact(name, tel_number)
    print('Added contact "{}, {}"'.format(result.name, result.phone))


def remove(first_name, last_name):
    name = '{} {}'.format(first_name, last_name)
    result = delete_contact(name)
    if result is not None:
        print('Removed contact "{}, {}"'.format(result.name, result.phone))
    else:
        print('Unknown contact "{}"'.format(name))


def find(request):
    result = find_contact(request)
    if result is not None:
        print('Found for "{}":'.format(request))
        print('\t- "{}, {}"'.format(result.name, result.phone))
    else:
        print('No results for "{}"'.format(request))


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

