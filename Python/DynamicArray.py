class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity

    def insert(self, index, value):
        # check if we have enough capacity
        if self.count >= self.capacity:
            # if not, add more capacity
            self.resize()
        # shift over evry item after index to the right by one
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        # add new value to the index
        self.storage[index] = value
        # increment count
        self.count += 1

    def append(self, value):
        # check if we have enough capacity
        if self.count >= self.capacity:
            # if not, add more capacity
            self.resize()
        # add new value to the index
        self.storage[self.count] = value
        # increment count
        self.count += 1

    def resize(self):
        # double capacity
        self.capacity *= 2
        # Allocate a new storage array with double capacity
        new_storage = [None] * self.capacity
        # copy all elements from old storage to new array
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
