import mysql.connector
from mysql.connector import errorcode

from app.models import Contact


class Storage:
    # def add_contact(self, contact: Contact) -> bool:
    def add_contact(self, contact):
        raise NotImplementedError()

    # def remove_contact(self, contact: Contact) -> bool:
    def remove_contact(self, contact):
        raise NotImplementedError()

    # def find_contacts(self, query: str) -> List[Contact]:
    def find_contacts(self, query):
        raise NotImplementedError()

    # def clear_contacts(self) -> bool:
    def clear_contacts(self):
        raise NotImplementedError()


class MemoryStorage(Storage):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.key] = contact
        return True

    def remove_contact(self, contact):
        if contact.key in self.contacts:
            del self.contacts[contact.key]
            return True
        return False

    def find_contacts(self, query):
        return [contact for key, contact in self.contacts.items() if query in key]

    def clear_contacts(self):
        self.contacts = {}


class FileStorage(Storage):
    def __init__(self, filename):
        self.filename = filename
        open(self.filename, 'a').close()


    def load_contacts_from_file(self, filename):
        book = {}
        with open(filename) as f:
            # lines = f.readlines()
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                for i in range(len(line)):
                    if line[i] == ';':
                        book[line[:i]] = line[i+1:]

        return book


    def add_contact(self, contact):
        book = self.load_contacts_from_file(self.filename)
        book[contact.name] = contact.phone

        with open(self.filename, 'w') as f:
            for name, phone in book.items():
                f.write('{};{}\n'.format(name, phone))
        return True


    def remove_contact(self, contact):
        book = self.load_contacts_from_file(self.filename)

        for client_name in book.keys():
            if client_name == contact.name:
                result = Contact(client_name, book[client_name])
                del book[client_name]

                with open(self.filename, 'w') as f:
                    for key, value in book.items():
                        f.write('{};{}\n'.format(key, value))
                return result


    def find_contacts(self, query):
        book = self.load_contacts_from_file(self.filename)
        result = []

        for name, phone in book.items(): # Поиск по значению - 999
            if query in book[name]:
                result.append(Contact(name, book[name]))

        for client_name in book.keys(): # Поиск по ключу - часть имени - John
            if query in client_name:
                result.append(Contact(client_name, book[client_name]))

        return result


    def clear_contacts(self):
        book = self.load_contacts_from_file(self.filename)
        with open(self.filename, 'w') as f:
            f.write('')


class SqlStorage(Storage):
    def __init__(self, host, user, password, database):
        self.cnx = mysql.connector.connect(
            host=host, user=user, password=password, database=database)


    def __del__(self):
        self.cnx.cursor().close()
        self.cnx.close()


    def add_contact(self, contact):
        query = 'INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)'
        data = ('John', 'Doe', '+79999999999')
        self.cnx.cursor().execute(query, data)
        self.cnx.commit()
        return True
