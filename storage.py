'''Вынести операции по работе с файлом в отдельный модуль.
Реализовать в файле storage.py функции:

 add_contact(first_name, last_name, phone_number)
 delete_contact(first_name, last_name)
 delete_all_contacts()
 find_contact(query)
Нигде, кроме этого файла, не должны использоваться функции os.remove и open.'''

from functions import load_contacts_from_file


filename = 'book.txt'

def add_contact(name, phone_number):
    book = load_contacts_from_file(filename)
    book[name] = phone_number

    with open(filename, 'w') as f:
        for key, value in book.items():
            f.write('{};{}\n'.format(key, value))


def delete_contact(name):
    book = load_contacts_from_file(filename)
    result = None

    for client_name in book.keys():
        if client_name == name:
            result = {
                'name': name,
                'phone': book[client_name]
            }
            del book[client_name]

            with open(filename, 'w') as f:
                for key, value in book.items():
                    f.write('{};{}\n'.format(key, value))
            break

    return result


def delete_all_contacts():
    with open(filename, 'w') as f:
        f.write('')


def find_contact(query):
    book = load_contacts_from_file(filename)
    result = None

    for key, numbers in book.items(): # Поиск по значению - 999
        if query in book[key]:
            result = {
                'name': key,
                'phone': book[key]
            }
            return result

    for client_name in book.keys(): # Поиск по ключу - часть имени - John
        if query in client_name:
            result = {
                'name': client_name,
                'phone': book[client_name]
            }
            return result






