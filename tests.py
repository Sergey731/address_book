from commands import add, remove, find
from storage import delete_all_contacts, find_contact, add_contact, delete_contact


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

    add_contact('John Doe', '+79999999999')
    add_contact('Max Payne', '+78888888888')

    delete_contact('John Doe')

    with open('book.txt') as f:
        expected = 'Max Payne;+78888888888\n'
        actual = f.read()

        print("* Removes one contact of two from file: {}".format(expected == actual))


def testFindOneContactByPartOfContact():
    delete_all_contacts()

    add_contact('John Doe', '+79999999999')
    add_contact('Max Payne', '+78888888999')

    result = find_contact('John')
    expectation = (result.name == 'John Doe')
    print(expectation)

    result = find_contact('888')
    expectation = (result.phone == '+78888888999')
    print(expectation)

    result = find_contact('Peter')
    expectation = (result is None)
    print(expectation)



# testAddContact()
# testAddTwoContacts()
# testRemoveContact()
testRemoveOneContactOfTwo()
# testFindOneContactByPartOfContact()
