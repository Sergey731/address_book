from os import remove as remove_file

from commands import add, remove


def testAddContact():
    remove_file('book.txt')

    add('John', 'Doe', '+79999999999')

    with open('book.txt') as f:
        expected = 'John Doe;+79999999999\n'
        actual = f.read()

        print("* Adds contact to file: {}".format(expected == actual))
testAddContact()


def testAddTwoContacts():
    remove_file('book.txt')

    add('John', 'Doe', '+79999999999')
    add('Max', 'Payne', '+78888888888')

    with open('book.txt') as f:
        expected = 'John Doe;+79999999999\nMax Payne;+78888888888\n'
        actual = f.read()

        print("* Adds two contacts to file: {}".format(expected == actual))
testAddTwoContacts()


def testRemoveContact():

    remove('John', 'Doe')

    with open('book.txt') as f:
        expected = ''
        actual = f.read()

        print("* Removes one contact from file: {}".format(expected == actual))
# testRemoveContact()


def testRemoveOneContactOfTwo():

    remove('John', 'Doe')

    with open('book.txt') as f:
        expected = 'Max Payne;+78888888888\n'
        actual = f.read()

        print("* Removes one contact of two from file: {}".format(expected == actual))
testRemoveContact()
