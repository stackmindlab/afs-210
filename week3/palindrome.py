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


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]


def isPalindrome(string):
    my_stack = Stack()
    queue = Queue()

    for character in string:
        my_stack.push(character)
        queue.enqueue(character)

    while not my_stack.isEmpty():
        if my_stack.pop() != queue.dequeue():
            return False

    return True

print(isPalindrome("racecar"))  # expected output: True
print(isPalindrome("noon"))    # expected output: True
print(isPalindrome("python"))  # expected output: False
print(isPalindrome("madam"))   # expected output: True
