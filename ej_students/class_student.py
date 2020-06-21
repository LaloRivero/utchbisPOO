class Student:
    def __init__(self, name, last_name, group, id):
        self.name = name
        self.last_name = last_name
        self.group = group
        self.id = id

    def to_dict(self):
        return vars(self)

    def show_first_name(self):
        print(self.name)

    def show_last_name(self):
        print(self.last_name)

    def show_len_of_full_name(self):
        print(len(self.name + self.last_name))
