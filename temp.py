import sys

filename = 'book.txt'

if sys.argv[1] == 'add':
    name = str(sys.argv[2]) + ' ' + str(sys.argv[3]) + str(sys.argv[4])
    print('Added contact ' + '"' + str(sys.argv[2]) + ' ' + str(sys.argv[3]) + ', ' + str(sys.argv[4]) + '"')

    with open(filename, 'a') as file_object:
        file_object.write(name +'\n')

elif sys.argv[1] == 'remove':
    with open(filename) as file_object:
        lines = file_object.readlines()
        book = {}
        book = {}

        for line in lines:
            for i in range(len(line)):
                if line[i] == '+':
                    book[line[:i]] = line[i:]

        for client_name in book.keys():
            if client_name == str(sys.argv[2]) + ' ' + str(sys.argv[3]):
                print("Removed contact " + '"' + str(sys.argv[2]) + ' ' + str(sys.argv[3]) + ', ' + str(book[client_name]).strip() + '"')
                del book[client_name]
                break
        else:
            print("Unknown contact " + '"' + str(sys.argv[2]) + ' ' + str(sys.argv[3]) + '"')

    with open(filename, 'w') as file_object:
        for key, value in book.items():
            file_object.write(key + value)

elif sys.argv[1] == 'find':
    with open(filename) as file_object:
        lines = file_object.readlines()
        book = {}

    for line in lines:
        for i in range(len(line)):
            if line[i] == '+':
                book[line[:i]] = line[i:]

    for key, numbers in book.items():#Поиск по значению - 999
        if sys.argv[2] in book[key]:
            print("Found for " +  '"' + sys.argv[2] + '":\n\t' + '"' + key + ', ' + numbers.strip() + '"')
            break

    for client_name in book.keys():#Поиск по ключу - часть имени - John
        for part_name in client_name.split():
            if part_name == str(sys.argv[2]):
                print("Found for " + part_name + ':' + '\n\t- "' + client_name + ', ' + str(book[client_name]).strip() + '"')
                break
        # else:
        #     print("No results for " + '"' + str(sys.argv[2]) + '"')






















