def load_contacts_from_file(filename):
    book = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            for i in range(len(line)):
                if line[i] == ';':
                    book[line[:i]] = line[i+1:].strip()
    return book


