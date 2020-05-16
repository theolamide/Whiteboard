class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    LList = LinkedList()

    # Create the nodes
    LList.head = Node(5)
    second = Node(87)
    third = Node(100)

    # Connect the nodes
    LList.head.next = second
    second.next = third

    # Print the LinkedList
    while LList.head != None:
        print("", LList.head.data, "->", end=' None')
        LList.head = LList.head.next


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# if __name__ == '__main__':
#     # Create the nodes
#     ListNode.val = ListNode(5)
#     second = ListNode(87)
#     third = ListNode(100)

#     # Connect the nodes
#     ListNode.next = second
#     second.next = third

#     # Print the LinkedList
#     while ListNode.val != None:
#         print("", ListNode.val, "->", end=' None')
#         ListNode.val = ListNode.val.next

# ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
