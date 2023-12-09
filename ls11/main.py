from random import randint


class Node:
    """
    _summary_ Node class 
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def pop(self, index=None):
        if index is None or index == 0:
            if not self.head:
                raise IndexError("Linked list is empty")
            popped = self.head
            self.head = self.head.next
            return popped.data
        current = self.head
        prev = None

        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            prev = current
            current = current.next
        popped = current
        prev.next = current.next
        return popped

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            index += 1
            current = current.next
        return -1

    def sort(self):
        if self.head is None:
            return

        current = self.head
        while current:
            runner = current.next
            while runner:
                if current.data > runner.data:
                    current.data, runner.data = runner.data, current.data
                runner = runner.next
            current = current.next

    def __str__(self):
        linked_list = []
        current = self.head

        while current:
            linked_list.append(str(current.data))
            current = current.next

        return ' -> '.join(linked_list)


ll = LinkedList()
ll.append(456)
for i in range(1, 16):
    ll.append(randint(1, 100))
print(ll)
ll.sort()
ll.remove(10)
ll.remove(100)
print(ll)
ll.pop()
ll.pop(0)
ll.pop(3)
print(ll)
print(ll.search(456))
