import sys
from functions import make_dict

filename = 'book.txt'
command = sys.argv[1]
first_name = str(sys.argv[2])

if command == 'add':
    last_name = str(sys.argv[3])
    tel_number = str(sys.argv[4])
    client_information = first_name + ' ' + last_name + '; ' + tel_number
    print('Added contact ' + '"' + client_information + '"')

    with open(filename, 'a') as file_object:
        file_object.write(client_information +'\n')

elif command == 'remove':
    last_name = str(sys.argv[3])

    with open(filename) as file_object:
        lines = file_object.readlines()
        book = make_dict(lines)

        for client_name in book.keys():
            if client_name == first_name + ' ' + last_name:
                print("Removed contact " + '"' + first_name + ' ' + last_name + str(book[client_name]).strip() + '"')
                del book[client_name]
                break
        else:
            print("Unknown contact " + '"' + first_name + ' ' + last_name + '"')

    with open(filename, 'w') as file_object:
        for key, value in book.items():
            file_object.write(key + value)

elif command == 'find':
    with open(filename) as file_object:
        lines = file_object.readlines()
        book = make_dict(lines)

    counter = 0
    for key, numbers in book.items(): # Поиск по значению - 999
        if first_name in book[key]:
            counter += 1
            print("Found for " +  '"' + first_name + '":\n\t' + '"' + key + numbers.strip() + '"')
            break

    for client_name in book.keys(): # Поиск по ключу - часть имени - John
        if first_name in client_name.split():
            print("Found for " + first_name + ':' + '\n\t- "' + client_name + str(book[client_name]).strip() + '"')
            break
        elif first_name not in client_name.split() and counter == 0:
            print("No results for " + '"' + first_name + '"')





