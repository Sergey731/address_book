'''Создать отдельный файл storage2.py и реализовать в нём перечисленные ниже функции и классы.
Создать файл test2.py и написать в нём тесты для функций модуля.
def add_contact(name, phone)
Описание: функция создаёт контакт с заданным именем и телефоном и сохраняет его в текстовый файл book.txt.
Параметры:

name: String – полное имя пользователя ("John Doe")
phone: String – номер телефона пользователя ("+7999")
Возвращаемое значение:
contact: Contact – созданный контакт

class Contact
Конструкторы:
Contact(name, phone)
Свойства:
name: String – полное имя пользователя ("John Doe")
phone: String – номер телефона пользователя ("+7999")
Методы: нет'''
from functions import load_contacts_from_file


filename = 'book.txt'

class Contact():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


def add_contact(name, phone):
    book = load_contacts_from_file(filename)
    book[name] = phone
    contact = Contact(name, phone)

    with open(filename, 'w') as f:
        for key, value in book.items():
            f.write('{};{}\n'.format(key, value))

    return contact

first_contact = add_contact('Ron Penn', '+79999997777')
print(first_contact.name, first_contact.phone)


# first_contact = Contact('John Doe', '+7999')
# print(first_contact.name, first_contact.phone)


