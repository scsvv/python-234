# class Person:
#     def __init__(self, name, date_of_birthday):
#         self.name = name
#         self.date_of_birthday = date_of_birthday

#     def calc_age(self):
#         today = datetime.today()
#         dob = datetime.strptime(self.date_of_birthday, "%Y-%m-%d")
#         return today.year - dob.year


# p1 = Person("George", "2001-12-16")
# print(p1.calc_age())


# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def size(self):
        return len(self.items)
