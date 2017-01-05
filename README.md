Адресная книга
==============

Написать консольную утилиту для работы с адресной строкой.

Программа должна предоставлять следующие возможности:

- добавление новой записи в адресную книгу
- удаление записи из адресной книги
- поиск записей в адресной книге

Примеры использования
---------------------

Добавление записи

```
$ address_book add John Doe +79999999999
Added contact "John Doe, +79999999999"
```

Удаление записи

```
$ address_book remove Max Payne
Unknown contact "Max Payne"

$ address_book remove John Doe
Removed contact "John Doe, +79999999999"
```

Поиск записей

```
$ address_book find Max
No results for "Max"

$ address_book find John
Found for "John":
  - "John Doe, +79999999999"

$ address_book find 999
Found for "999":
  - "John Doe, +79999999999"
```
