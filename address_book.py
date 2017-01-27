import sys
from app.commands import add, remove, find, help


command = sys.argv[1]

if command == 'add':
    add(sys.argv[2], sys.argv[3], sys.argv[4])

elif command == 'remove':
    remove(sys.argv[2], sys.argv[3])

elif command == 'find':
    find(sys.argv[2])

elif command == 'help':
    help()

