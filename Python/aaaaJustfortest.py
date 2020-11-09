from collections import OrderedDict
# def toList(string):

#     theList = list(string)

#     print(theList)


# a = "The world is on fire"
# b = 10
# toList("ABCDREDD")
# toList(str(b))
# toList(a)

# def toListTwo(string):
#     List = list(str(string))
#     IntLast = int(List[-1])
#     print(type(IntLast), IntLast)

# b = 10
# toListTwo(b)


# def arrayPrint(a):
#     freqObj = {}
#     flag = True

#     for element in a:
#         flag = False
#         if element in freqObj.keys():
#             print(element)
#             return element
#         else:
#             freqObj[element] = 1
#         flag = True

#     if flag:
#         print(-1)
#         return -1


# test_list = [1, 2, 3, 6, 7]
# arrayPrint(test_list)

# # printing original list
# print("The original list is : " + str(test_list))

# # insert element
# k = 5

# # using naive method
# # insertion in sorted list
# # using naive method
# for i in range(len(test_list)):
#     if test_list[i] > k:
#         index = i
#         print(index)
#         print(i)
#         break
# res = test_list[:i] + [k] + test_list[i:]
# print(res)

# def staircase(n):
#     spaces = n-1
#     hashes = 1
#     while spaces >= 0:
#         print(spaces*" " + hashes*"#")
#         spaces -= 1
#         hashes += 1


# staircase(100)


# def firstNotRepeatingCharacter(s):
#     freqObj = OrderedDict()

#     for element in s:
#         if element in freqObj:
#             freqObj[element] += 1
#         else:
#             freqObj[element] = 1

#     for key in freqObj:
#         if freqObj[key] == 1:
#             return key

#     return "_"


# charac = "charcater"
# firstNotRepeatingCharacter(charac)
def List(arr):
    arr1 = []
    for i in range(0, len(arr)):
        val = arr[i]*1000
        arr1.append(val)

    print(arr1)


num = [2, 3, 4]
List(num)
