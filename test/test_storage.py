import unittest

from code.models import Contact
from code.storage import MemoryStorage


class TestMemoryStorage(unittest.TestCase):

    def test_storage(self):
        storage = MemoryStorage()

        john = Contact('John', 'Doe', '+79999999999')
        storage.add_contact(john)
        result = storage.find_contacts('John')
        self.assertEqual(len(result), 1)

        julie = Contact('Julie', 'Doe', '+79999999999')
        storage.add_contact(julie)
        result = storage.find_contacts('Doe')
        self.assertEqual(len(result), 2)

        john = Contact('John', 'Doe', '+79999999999')
        storage.add_contact(john)
        result = storage.find_contacts('John')
        self.assertEqual(len(result), 1)

        john = Contact('John', 'Doe', '+79999999999')
        storage.remove_contact(john)
        result = storage.find_contacts('John')
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
