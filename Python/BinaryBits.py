def hammingDistance(x, y):
    """
        :type x: int
        :type y: int
        :rtype: int
        """
    # Do an exclusive or
    exclusive_xy = x ^ y
    count = 0

    while exclusive_xy > 0:
        if (exclusive_xy % 2) == 0:
            exclusive_xy = exclusive_xy >> 1
        else:
            count += 1
            exclusive_xy = exclusive_xy >> 1

    print("count", count)


hammingDistance(4, 1)
hammingDistance(10, 1)
hammingDistance(10, 0)
hammingDistance(0, 0)
hammingDistance(5, 2)
hammingDistance(3, 3)

# Brute for method
# x_num = [char for char in bin(x)]
# y_num = [char for char in bin(y)]
# count = 0
# print("x", x_num)
# print("y", y_num)
# for i in range(len(x_num)):
#     if x_num[i] != y_num[i]:
#         count += 1
#         print(count)
#         return count
#     else:
#         print(count)
#         return count
