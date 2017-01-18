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


    def test_add_contact(self):
        storage = MemoryStorage()
        john = Contact('John Doe', '+7999')

        storage.add_contact(john)
        results = storage.find_contacts('John Doe')

        self.assertEqual(len(results), 1)
        self.assertEqual(john.name, results[0].name)


    def test_remove_contact(self):
        pass

    # дописать тесты для всех методов
    # можно даже по несколько тестов на метод


if __name__ == '__main__':
    unittest.main()
