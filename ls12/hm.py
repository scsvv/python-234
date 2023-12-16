class Student:
    def __init__(self, name, surname, form, age):
        self.name = name
        self.surname = surname
        self.form = form
        self.age = age
        self.subjects = dict()

    def __str__(self):
        return f"{self.surname} {self.name} {self.age}"

    def check_subject(self, subject):
        if subject in self.subjects.keys():
            return True
        return False

    def add_subject(self, subject=None):
        if subject is None or self.check_subject(subject):
            return

        self.subjects.setdefault(subject, list())

    def add_marks(self, subject=None, marks=None):
        if subject is None or marks is None:
            return None
        if not isinstance(marks, list):
            return
        if not self.check_subject(subject):
            return

        self.subjects[subject] += marks

    def calculate_mark_avarage(self, subject=None):
        if subject is None or not self.check_subject(subject):
            return

        return sum(self.subjects[subject]) / len(self.subjects[subject])


alex = Student("Alex", "A", "7A", 13)
maxim = Student("Max", "B", "7B", 13)

alex.add_subject("history")
alex.add_marks("history", [12, 10, 11])
alex.add_marks("history", [12, 10, 11])
print(alex.calculate_mark_avarage("history"))

print(alex.subjects)
