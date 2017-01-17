class Contact():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @property
    def key(self):
        return "{}_{}".format(self.name, self.phone)
