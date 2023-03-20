class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

class Queue