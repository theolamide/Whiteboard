# def testString(string):
#     toCheck = []
#     # print(len(string))
#     # print(string[0])
#     for i in range(0, len(string)):
#         if string[i].isalnum() is False:
#             toCheck.append(string[i])

#     print(0 % 2)
#     print(toCheck)


# A = "akjfdwfiuhqiunfwaejf7918324r01[qnfwoijfj>ioqfhiw{)(()"
# testString("fire")
# testString(A)


def find3Numbers(arr, target):
    # A.sort()
    # print(A)
    # arr_size = len(A)
    # for i in range(0, arr_size-1):
    #     # Find pair in subarray A[i + 1..n-1]
    #     # with sum equal to sum - A[i]
    #     s = set()
    #     curr_sum = sum - A[i]
    #     for j in range(i + 1, arr_size):
    #         if (curr_sum - A[j]) in s:
    #             print("Triplet is", A[i],
    #                   ", ", A[j], ", ", curr_sum-A[j])
    #             return True
    #         s.add(A[j])
    # print("False")
    # return False

    arr.sort()
    outputArray = list()
    for i in range(0, len(arr)-1):
        s = set()
        current_sum = target - arr[i]
        for j in range(i+1, len(arr)):
            if (current_sum - arr[j]) in s:
                outputArray.append([arr[i], arr[j], current_sum])
                print(outputArray)

    print(outputArray)
    return(outputArray)


A = [2, 4, 1, 5, 6, 8]
find3Numbers(A, 7)


# def insertNodeAtPosition(head, data, position):
#     LL = head
#     count = 0
#     NewNode = SinglyLinkedListNode(data)
#     PreviousNode = head

#     while count < position:
#         PreviousNode = LL
#         LL = LL.next
#         count += 1

#     NextNext = PreviousNode.next
#     PreviousNode.next = NewNode
#     NewNode.next = NextNext

#     return head
