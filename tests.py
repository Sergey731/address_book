from os import remove

from commands import add


def testAddContact():
	remove('book.txt')

	add('John', 'Doe', '+79999999999')

	with open('book.txt') as f:
		expected = 'John Doe;+79999999999\n'
		actual = f.read()

		print("* Adds contact to file: {}".format(expected == actual))
testAddContact()


def testAddTwoContacts():
	remove('book.txt')

	add('John', 'Doe', '+79999999999')
	add('Max', 'Payne', '+78888888888')

	with open('book.txt') as f:
		expected = 'John Doe;+79999999999\nMax Payne;+78888888888\n'
		actual = f.read()

		print("* Adds two contacts to file: {}".format(expected == actual))
testAddTwoContacts()


def testRemoveContact():
	pass
testRemoveContact()


def testRemoveOneContactOfTwo():
	pass
testRemoveContact()
