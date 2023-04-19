class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        # Insert your hashing function code
        return key % self.size

    def rehash(self, key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self, key, data):
        # Insert your code here to store key and data
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                rehashValue = self.rehash(key)
                if self.slots[rehashValue] is None:
                    self.slots[rehashValue] = key
                    self.data[rehashValue] = data
                else:
                    print("Unresolved, Data Was Lost.")

    def get(self, key):
        # Insert your code here to get data by key
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = (position + self.rehash(key)) % self.size
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# Store the Items in the table below

H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)

# print the data values
print(H.data)

# print the value for key 52
print(H[52])
