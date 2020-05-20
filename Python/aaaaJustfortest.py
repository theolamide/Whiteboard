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

test_list = [1, 2, 3, 6, 7]

# printing original list
print("The original list is : " + str(test_list))

# insert element
k = 5

# using naive method
# insertion in sorted list
# using naive method
for i in range(len(test_list)):
    if test_list[i] > k:
        index = i
        print(index)
        print(i)
        break
res = test_list[:i] + [k] + test_list[i:]
print(res)
