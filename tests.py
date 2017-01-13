from commands import add, remove
from storage import delete_all_contacts
from models import Contact


def testAddContact():
    delete_all_contacts()

    add('John', 'Doe', '+79999999999')

    with open('book.txt') as f:
        expected = 'John Doe;+79999999999\n'
        actual = f.read()

        print("* Adds contact to file: {}".format(expected == actual))


def testAddTwoContacts():
    delete_all_contacts()

    add('John', 'Doe', '+79999999999')
    add('Max', 'Payne', '+78888888888')

    with open('book.txt') as f:
        expected = 'John Doe;+79999999999\nMax Payne;+78888888888\n'
        actual = f.read()

        print("* Adds two contacts to file: {}".format(expected == actual))


def testRemoveContact():
    delete_all_contacts()

    add('John', 'Doe', '+79999999999')

    remove('John', 'Doe')

    with open('book.txt') as f:
        expected = ''
        actual = f.read()

        print("* Removes one contact from file: {}".format(expected == actual))


def testRemoveOneContactOfTwo():
    delete_all_contacts()

    add('John', 'Doe', '+79999999999')
    add('Max', 'Payne', '+78888888888')

    remove('John', 'Doe')

    with open('book.txt') as f:
        expected = 'Max Payne;+78888888888\n'
        actual = f.read()

        print("* Removes one contact of two from file: {}".format(expected == actual))

def testContact():
    john = Contact('John Doe', '+79999999999')

    if john.name == 'John Doe' and john.phone == '+79999999999':
        print("* Contact created")
    else:
        print("* Contact not created")


testAddContact()
testAddTwoContacts()
testRemoveContact()
testRemoveOneContactOfTwo()
testContact()
