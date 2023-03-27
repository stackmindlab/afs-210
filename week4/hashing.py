class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        return key % self.size

    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self,key,data):
        # Insert your code here to store key and data 
        hashValue = self.hashfunction(key)
        rehashValue = self.rehash(key)

        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = data

    def get(self,key):
        # Insert your code here to get data by key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()

# Store remaining input data
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

