import unittest

from storage2 import MemoryStorage
from models import Contact

'''
    python3 -m unittest discover
'''
class TestMemoryStorage(unittest.TestCase):
    def test_creation(self):
        storage = MemoryStorage()

        self.assertTrue(isinstance(storage, MemoryStorage))
        self.assertTrue(type(storage) == MemoryStorage)


    def test_add_contact(self):
        storage = MemoryStorage()
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        results = storage.find_contacts('John Doe')

        self.assertEqual(len(results), 1)
        self.assertEqual(john.name, results[0].name)

        storage.add_contact(tom)
        results = storage.find_contacts('+7888')

        self.assertEqual(len(results), 1)
        self.assertEqual(tom.phone, results[0].phone)
        self.assertEqual(tom.phone[:2], john.phone[:2])
        self.assertNotEqual(tom.phone[:3], john.phone[:3])
        self.assertNotEqual(john.phone, '+7888')
        self.assertNotEqual(john.key, tom.key)


    def test_remove_contact(self):
        storage = MemoryStorage()
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.remove_contact(john)
        results = storage.find_contacts('Tom Pen')

        self.assertTrue(results)

        self.assertEqual(len(results), 1)
        self.assertEqual(tom.name, results[0].name)

        results = storage.find_contacts('John Doe')
        self.assertFalse(results)


    def test_find_contacts(self):
        storage = MemoryStorage()
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        results = storage.find_contacts('Tom Pen')
        self.assertTrue(results)

        results = storage.find_contacts('+7999')
        self.assertTrue(results)

        results = storage.find_contacts('+7555')
        self.assertFalse(results)


    def test_clear_contacts(self):
        storage = MemoryStorage()
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.clear_contacts()

        results = storage.find_contacts('John Doe')
        self.assertFalse(results)

        results = storage.find_contacts('Tom Pen')
        self.assertFalse(results)


    # дописать тесты для всех методов
    # можно даже по несколько тестов на метод


if __name__ == '__main__':
    unittest.main()
