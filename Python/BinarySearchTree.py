class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new< node.value
        if value < self.value:
            # if left does not exist
            if self.left is None:
                # create left
                self.left = BinarySearchTree(value)
                # call insert again
            else:
                self.left.insert(value)
        else:  # value is greater than or equal to
            # If right does not exist
            if self.right is None:
                # Create right
                self.right = BinarySearchTree(value)
            else:
                # call insert again
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft = Queue()
        bft.enqueue(self)
        while bft.size > 0:
            node = bft.dequeue()
            print(node.value)
            if node.left is not None:
                bft.enqueue(self.left)
            if node.right is not None:
                bft.enqueue(self.right)

            # Print the value of every node, starting with the given node,
            # in an iterative depth first traversal
    def dft_print(self, node):
        dft = Stack()
        dft.push(self)
        while dft.size > 0:
            node = dft.pop()
            print(node.value)
            if node.left is not None:
                dft.push(self.left)
            if node.right is not None:
                dft.push(self.right)
