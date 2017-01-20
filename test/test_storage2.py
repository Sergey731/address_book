import unittest

from storage2 import MemoryStorage, FileStorage
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
        tom = Contact('Tom Len', '+7888')

        storage.add_contact(john)
        results = storage.find_contacts('John Doe')

        self.assertEqual(len(results), 1)
        self.assertEqual(john.name, results[0].name)

        storage.add_contact(tom)
        results = storage.find_contacts('+7888')

        self.assertEqual(len(results), 1)
        self.assertEqual(tom.phone, results[0].phone)

        self.assertNotEqual(john.key, tom.key)


    def test_remove_contact(self):
        storage = MemoryStorage()
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.remove_contact(john)
        results = storage.find_contacts('Tom Pen')

        self.assertEqual(len(results), 1)
        self.assertEqual(tom.name, results[0].name)

        results = storage.find_contacts('John Doe')
        self.assertEqual(len(results), 0)


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

        results = storage.find_contacts('+7')
        self.assertEqual(len(results), 2)


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


class TestFileStorage(unittest.TestCase):
    def test_creation(self):
        storage = FileStorage('book.txt')

        self.assertTrue(isinstance(storage, FileStorage))
        self.assertTrue(type(storage) == FileStorage)


    def test_add_contact(self):
        storage = FileStorage('book.txt')
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        results = storage.find_contacts('John Doe')

        self.assertEqual(results.name, 'John Doe')
        self.assertEqual(john.name, results.name)

        storage.add_contact(tom)
        results = storage.find_contacts('+7888')

        self.assertEqual(results.phone, '+7888')
        self.assertEqual(tom.phone, results.phone)

        self.assertNotEqual(john.key, tom.key)

        storage.delete_all_contacts()


    def test_remove_contact(self):
        storage = FileStorage('book.txt')
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.delete_contact(john)

        results = storage.find_contacts('Tom Pen')
        self.assertTrue(results)

        results = storage.find_contacts('+7888')
        self.assertTrue(results)

        results = storage.find_contacts('+7999')
        self.assertFalse(results)

        storage.delete_all_contacts()


    def test_find_contacts(self):
        storage = FileStorage('book.txt')
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

        # results = storage.find_contacts('+7')
        # self.assertEqual(results.phone, 2)

        storage.delete_all_contacts()


    def test_clear_contacts(self):
        storage = FileStorage('book.txt')
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.delete_all_contacts()

        results = storage.find_contacts('John Doe')
        self.assertFalse(results)

        results = storage.find_contacts('Tom Pen')
        self.assertFalse(results)



    # дописать тесты для всех методов
    # можно даже по несколько тестов на метод


if __name__ == '__main__':
    unittest.main()
