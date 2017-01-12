'''Вынести операции по работе с файлом в отдельный модуль.
Реализовать в файле storage.py функции:

 add_contact(first_name, last_name, phone_number)
 delete_contact(first_name, last_name)
 delete_all_contacts()
 find_contact(query)
Нигде, кроме этого файла, не должны использоваться функции os.remove и open.

Дополнительное условие: сочетание имени и фамилии в файле должно быть уникальным. При добавлении контакта с
уже существующими именем и фамилией он должен записываться вместо существующей записи.'''
