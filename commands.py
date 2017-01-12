from functions import load_contacts_from_file


filename = 'book.txt'


def add(first_name, last_name, tel_number):
    print('Added contact "{} {}, {}"'.format(first_name, last_name, tel_number))
    with open(filename, 'a') as f:
        f.write('{} {};{}\n'.format(first_name, last_name, tel_number))


def remove(first_name, last_name):
    book = load_contacts_from_file(filename)

    for client_name in book.keys():
        if client_name == '{} {}'.format(first_name, last_name):
            print('Removed contact "{} {}, {}"'.format(first_name, last_name, book[client_name]))
            del book[client_name]

            with open(filename, 'w') as f:
                for key, value in book.items():
                    f.write('{};{}\n'.format(key, value))

            break
    else:
        print('Unknown contact "{} {}"'.format(first_name, last_name))


def find(request):
    book = load_contacts_from_file(filename)

    counter = 0
    for key, numbers in book.items(): # Поиск по значению - 999
        if request in book[key]:
            counter += 1
            print('Found for "{}":'.format(request))
            print('\t- "{}, {}"'.format(key, numbers))
            break

    for client_name in book.keys(): # Поиск по ключу - часть имени - John
        if request in client_name.split():
            print('Found for "{}":'.format(request))
            print('\t- "{}, {}"'.format(client_name, book[client_name]))

            break
        elif request not in client_name.split() and counter == 0:
            print('No results for "{}"'.format(request))
            break


def help():
    print(
    '''
    Commands:

    - add - adds a new entry in the address book
    - remove - removes the entry from the address book
    - find - is looking for an entry in the address book

    Examples:

    Record addition
    ...
    > python address_book.py add John Doe +79999999999
    Added contact "John Doe, +79999999999"
    ...

    Deleting records
    ...
    > python address_book.py remove Max Payne
    Unknown contact "Max Payne"

    > python address_book.py remove John Doe
    Removed contact "John Doe, +79999999999"
    ...

    Search records
    ...
    > python address_book.py find Max
    No results for "Max"

    > python address_book.py find John
    Found for "John":
        - "John Doe, +79999999999"

    > python address_book.py find 999
    Found for "999":
        - "John Doe, +79999999999"
    ...''')



