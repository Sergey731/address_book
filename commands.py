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
