import sys
from functions import load_contacts_from_file

filename = 'book.txt'
command = sys.argv[1]
first_name = sys.argv[2]

if command == 'add':
    def command_is_add(last_name, tel_number):

        print('Added contact "{0} {1}, {2}"'.format(first_name, last_name, tel_number))
        with open(filename, 'a') as f:
            f.write(first_name + ' ' + last_name + ';' + tel_number + '\n')
    command_is_add(sys.argv[3], sys.argv[4])

elif command == 'remove':
    def command_is_remove(last_name):

        book = load_contacts_from_file(filename)

        for client_name in book.keys():
            if client_name == first_name + ' ' + last_name:
                print('Removed contact "{0} {1}, {2}"'.format(first_name, last_name, book[client_name].strip()))
                del book[client_name]
                break
        else:
            print('Unknown contact "{0} {1}"'.format(first_name, last_name))

        with open(filename, 'w') as f:
            for key, value in book.items():
                f.write(key + value)
    command_is_remove(sys.argv[3])

elif command == 'find':
    def command_is_find(first_name):

        book = load_contacts_from_file(filename)

        counter = 0
        for key, numbers in book.items(): # Поиск по значению - 999
            if first_name in book[key]:
                counter += 1
                print('Found for "{0}": \n\t- "{1}, {2}"'.format(first_name, key, numbers.strip()))
                break

        for client_name in book.keys(): # Поиск по ключу - часть имени - John
            if first_name in client_name.split():
                print('Found for "{0}": \n\t- "{1}, {2}"'.format(first_name, client_name, book[client_name].strip()))
                break
            elif first_name not in client_name.split() and counter == 0:
                print('No results for "{0}"'.format(first_name))
                break
    command_is_find(first_name)




