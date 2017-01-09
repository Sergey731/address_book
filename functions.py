def make_dict(lines):
    book = {}
    for line in lines:
            for i in range(len(line)):
                if line[i] == ';':
                    book[line[:i]] = line[i:]

    return book
