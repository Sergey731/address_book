def load_contacts_from_file(filename):
    book = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            for i in range(len(line)):
                if line[i] == ';':
                    book[line[:i]] = line[i+1:]

    return book


