import os
import unittest

from app.models import Contact
from app.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from app.storage import SqlStorage



'''
    python3 -m unittest discover
'''
# class TestMemoryStorage(unittest.TestCase):
#     def test_creation(self):
#         storage = MemoryStorage()
#
#         self.assertTrue(isinstance(storage, MemoryStorage))
#         self.assertTrue(type(storage) == MemoryStorage)
#
#
#     def test_add_contact(self):
#         storage = MemoryStorage()
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Len', '+7888')
#
#         storage.add_contact(john)
#         results = storage.find_contacts('John Doe')
#
#         self.assertEqual(len(results), 1)
#         self.assertEqual(john.name, results[0].name)
#
#         storage.add_contact(tom)
#         results = storage.find_contacts('+7888')
#
#         self.assertEqual(len(results), 1)
#         self.assertEqual(tom.phone, results[0].phone)
#
#         self.assertNotEqual(john.key, tom.key)
#
#
#     def test_remove_contact(self):
#         storage = MemoryStorage()
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         storage.add_contact(tom)
#
#         storage.remove_contact(john)
#         results = storage.find_contacts('Tom Pen')
#
#         self.assertEqual(len(results), 1)
#         self.assertEqual(tom.name, results[0].name)
#
#         results = storage.find_contacts('John Doe')
#         self.assertEqual(len(results), 0)
#
#
#     def test_find_contacts(self):
#         storage = MemoryStorage()
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         storage.add_contact(tom)
#
#         results = storage.find_contacts('Tom Pen')
#         self.assertTrue(results)
#
#         results = storage.find_contacts('+7999')
#         self.assertTrue(results)
#
#         results = storage.find_contacts('+7555')
#         self.assertFalse(results)
#
#         results = storage.find_contacts('+7')
#         self.assertEqual(len(results), 2)
#
#
#     def test_clear_contacts(self):
#         storage = MemoryStorage()
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         storage.add_contact(tom)
#
#         storage.clear_contacts()
#
#         results = storage.find_contacts('John Doe')
#         self.assertFalse(results)
#
#         results = storage.find_contacts('Tom Pen')
#         self.assertFalse(results)


# class TestFileStorage(unittest.TestCase):
#     filename = 'book.txt'
#
#
#     def tearDown(self):
#         os.remove(self.filename)
#
#
#     def test_creation(self):
#         storage = FileStorage('book.txt')
#
#         self.assertTrue(isinstance(storage, FileStorage))
#         self.assertTrue(type(storage) == FileStorage)
#
#
#     def test_add_contact(self):
#         storage = FileStorage('book.txt')
#
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         results = storage.find_contacts('John Doe')
#
#         self.assertEqual(len(results), 1)
#         self.assertEqual(john.name, results[0].name)
#
#         storage.add_contact(tom)
#         results = storage.find_contacts('+7888')
#
#         self.assertEqual(len(results), 1)
#         self.assertEqual(tom.phone, results[0].phone)
#
#         self.assertNotEqual(john.key, tom.key)
#
#
#     def test_remove_contact(self):
#         storage = FileStorage('book.txt')
#
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         storage.add_contact(tom)
#
#         storage.remove_contact(john)
#         results = storage.find_contacts('Tom Pen')
#
#         self.assertEqual(len(results), 1)
#         self.assertEqual(tom.name, results[0].name)
#
#         results = storage.find_contacts('John Doe')
#         self.assertEqual(len(results), 0)
#
#
#     def test_find_contacts(self):
#         storage = FileStorage('book.txt')
#
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         storage.add_contact(tom)
#
#         results = storage.find_contacts('Tom Pen')
#         self.assertTrue(results)
#
#         results = storage.find_contacts('+7999')
#         self.assertTrue(results)
#
#         results = storage.find_contacts('+7555')
#         self.assertFalse(results)
#
#         results = storage.find_contacts('+7')
#         self.assertEqual(len(results), 2)
#
#
#     def test_clear_contacts(self):
#         storage = FileStorage('book.txt')
#
#         john = Contact('John Doe', '+7999')
#         tom = Contact('Tom Pen', '+7888')
#
#         storage.add_contact(john)
#         storage.add_contact(tom)
#
#         storage.clear_contacts()
#
#         results = storage.find_contacts('John Doe')
#         self.assertFalse(results)
#
#         results = storage.find_contacts('Tom Pen')
#         self.assertFalse(results)



class TestSqlStorage(unittest.TestCase):


    def test_creation(self):
        storage = SqlStorage(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
        storage.clear_contacts()

        self.assertTrue(isinstance(storage, SqlStorage))
        self.assertTrue(type(storage) == SqlStorage)


    def test_add_contact(self):
        storage = SqlStorage(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
        storage.clear_contacts()
        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Len', '+7888')

        storage.add_contact(john)
        results = storage.find_contacts('John')

        self.assertEqual(len(results), 1)
        self.assertEqual(john.name, results[0].name)

        storage.add_contact(tom)
        results = storage.find_contacts('+7888')

        self.assertEqual(len(results), 1)
        self.assertEqual(tom.phone, results[0].phone)

        self.assertNotEqual(john.key, tom.key)


    def test_remove_contact(self):
        storage = SqlStorage(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
        storage.clear_contacts()

        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.remove_contact(john)
        results = storage.find_contacts('Tom')

        self.assertEqual(len(results), 1)
        self.assertEqual(tom.name, results[0].name)

        results = storage.find_contacts('John')
        self.assertEqual(len(results), 0)


    def test_find_contacts(self):
        storage = SqlStorage(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
        storage.clear_contacts()

        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        results = storage.find_contacts('Pen')
        self.assertTrue(results)

        results = storage.find_contacts('John')
        self.assertTrue(results)

        results = storage.find_contacts('+7555')
        self.assertFalse(results)

        results = storage.find_contacts('+7')
        self.assertEqual(len(results), 2)


    def test_clear_contacts(self):
        storage = SqlStorage(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
        storage.clear_contacts()

        john = Contact('John Doe', '+7999')
        tom = Contact('Tom Pen', '+7888')

        storage.add_contact(john)
        storage.add_contact(tom)

        storage.clear_contacts()

        results = storage.find_contacts('John')
        self.assertFalse(results)

        results = storage.find_contacts('Pen')
        self.assertFalse(results)


if __name__ == '__main__':
    unittest.main()
