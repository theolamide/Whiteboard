class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def condense(head):
    # Write your code here
    toCheckFreq = {}
    LL = head

    toCheckFreq[head.data] = 1

    while LL is not None and LL.next is not None and LL.next:
        NextNode = LL.next
        if NextNode.data in toCheckFreq:
            # delete node
            NextNext = LL.next.next
            LL.next = NextNext  # reassign next value
        else:
            toCheckFreq[NextNode.data] = 1
            LL = LL.next

    print(toCheckFreq)
    return head


A = [3, 4, 3, 2, 6, 1, 2, 6]
head = None
current = None
for data in A:
    Node = SinglyLinkedListNode(data)
    if head == None:
        head = Node
        current = head
    else:
        current.next = Node
        current = Node

condense(head)
