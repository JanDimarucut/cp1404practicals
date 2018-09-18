class Person:

    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{} {}, {} years old".format(self.first_name, self.last_name, self.age)

    # def sort_list(self):