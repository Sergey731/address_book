from typing import List

from code.models import Contact


class Storage:
    def add_contact(self, contact: Contact) -> bool:
        raise NotImplementedError()
        
    def remove_contact(self, contact: Contact) -> bool:
        raise NotImplementedError()
        
    def find_contacts(self, query: str) -> List[Contact]:
        raise NotImplementedError()
        
    def clear_contacts(self) -> bool:
        raise NotImplementedError()


class MemoryStorage(Storage):
    def __init__(self):
        self.contacts = {};
    
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
    pass


class SqlStorage(Storage):
    pass
