from models import Contact
from functions import load_contacts_from_file


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


    def add_contact(self, contact):
        book = load_contacts_from_file(self.filename)
        book[contact.name] = contact.phone

        with open(self.filename, 'w') as f:
            for name, phone in book.items():
                f.write('{};{}\n'.format(name, phone))
        return True


    def remove_contact(self, contact):
        book = load_contacts_from_file(self.filename)

        for client_name in book.keys():
            if client_name == contact.name:
                result = Contact(client_name, book[client_name])
                del book[client_name]

                with open(self.filename, 'w') as f:
                    for key, value in book.items():
                        f.write('{};{}\n'.format(key, value))
                return result


    def find_contacts(self, query):
        book = load_contacts_from_file(self.filename)
        result = []

        for name, phone in book.items(): # Поиск по значению - 999
            if query in book[name]:
                result.append(Contact(name, book[name]))

        for client_name in book.keys(): # Поиск по ключу - часть имени - John
            if query in client_name:
                result.append(Contact(client_name, book[client_name]))

        return result


    def clear_contacts(self):
        book = load_contacts_from_file(self.filename)
        with open(self.filename, 'w') as f:
            f.write('')





class SqlStorage(Storage):
    pass
