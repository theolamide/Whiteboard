def hammingDistance(self, x, y):
    """
        :type x: int
        :type y: int
        :rtype: int
        """
    x_num = [char for char in bin(x)]
    y_num = [char for char in bin(y)]
    print(x_num, y_num)
    count = 0
    for i in range(len(x_num)):
        if x_num[i] != y_num[i]:
            count += 1
            print(i, count)
            return count


hammingDistance(0, 5, 7)
