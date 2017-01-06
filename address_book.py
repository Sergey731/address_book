import sys

filename = 'book.txt'
find_name = str(sys.argv[2]) + ' ' + str(sys.argv[3])

if sys.argv[1] == 'add':
    name = find_name + str(sys.argv[4])
    print('Added contact ' + '"' + find_name + ', ' + str(sys.argv[4]) + '"')

    with open(filename, 'a') as file_object:
        file_object.write(name +'\n')

elif sys.argv[1] == 'remove':
    with open(filename) as file_object:
        lines = file_object.readlines()
        book = {}

        for line in lines:
            for i in range(len(line)):
                if line[i] == '+':
                    book[line[:i]] = line[i:]

        for client_name in book.keys():
            if client_name == find_name:
                print("Removed contact " + '"' + find_name + ', ' + str(book[client_name]).strip() + '"')
                del book[client_name]
                break
        else:
            print("Unknown contact " + '"' + find_name + '"')

    with open(filename, 'w') as file_object:
        for key, value in book.items():
            file_object.write(key + value)






