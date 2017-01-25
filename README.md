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
> python address_book.py add John Doe +79999999999
Added contact "John Doe, +79999999999"
```

Удаление записи

```
> python address_book.py remove Max Payne
Unknown contact "Max Payne"

> python address_book.py remove John Doe
Removed contact "John Doe, +79999999999"
```

Поиск записей

```
> python address_book.py find Max
No results for "Max"

> python address_book.py find John
Found for "John":
  - "John Doe, +79999999999"

> python address_book.py find 999
Found for "999":
  - "John Doe, +79999999999"
```

virtualenv
----------

```
source ./python3_env/bin/activate
export PYTHONPATH=$(pwd)
```
