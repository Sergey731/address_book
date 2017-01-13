import unittest

from code.models import Contact


class TestContacts(unittest.TestCase):

    def test_contact_contains_name_and_phone(self):
        john = Contact('John', 'Doe', '+79999999999')
        self.assertEqual(john.first_name, 'John')
        self.assertEqual(john.last_name, 'Doe')
        self.assertEqual(john.phone_number, '+79999999999')

    def test_equal_contacts_has_equal_keys(self):
        john1 = Contact('John', 'Doe', '+79999999999')
        john2 = Contact('John', 'Doe', '+79999999999')
        self.assertEqual(john1.key, john2.key)

    def test_contacts_with_different_first_names_has_different_keys(self):
        john = Contact('John', 'Doe', '+79999999999')
        julie = Contact('Julie', 'Doe', '+79999999999')
        self.assertNotEqual(john.key, julie.key)

    def test_contacts_with_different_last_names_has_different_keys(self):
        john_doe = Contact('John', 'Doe', '+79999999999')
        john_payne = Contact('John', 'Payne', '+79999999999')
        self.assertNotEqual(john_doe.key, john_payne.key)

    def test_contacts_with_different_phone_numbers_has_different_keys(self):
        john_home = Contact('John', 'Doe', '+79999999999')
        john_mobile = Contact('John', 'Doe', '+78888888888')
        self.assertNotEqual(john_home.key, john_mobile.key)


if __name__ == '__main__':
    unittest.main()
