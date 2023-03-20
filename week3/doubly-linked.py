class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count

    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def addLast(self, data) -> None:
        # Add a node at the end of the list
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        if index < 0 or index > self.count:
            return
        elif index == 0:
            self.addFirst(data)
        elif  index > self.count:
            self.addLast(data)
            return
        else:
            new_node = Node(data)
            curr = self.head
            for i in range(1, index -1):
                curr = curr.next
            new_node.prev = curr
            new_node.next = curr.next
            curr.next.prev = new_node
            curr.next = new_node
            self.count += 1

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1
        curr = self.head
        index = 0
        while curr:
            if curr.data == data:
                return index
            curr = curr.next
            index += 1
        return -1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next.prev = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr



# Store the items in the list below in the order they are listed and then print the list
words = DoublyLinkedList()
words.addLast("May")
words.addLast("the")
words.addLast("Force")
words.addLast("be")
words.addLast("with")
words.addLast("you")
words.addLast("!")

# Print the list with print(words)
print(words)

# Return the index position of "with" in the list and print this value
index = words.indexOf("with")
print(index)

# Change "you" into "us" on the List
words[5] = "us"

# Add "all" before "!" on the list
words.addAtIndex("all", 7)

# Print the list
print(words)




