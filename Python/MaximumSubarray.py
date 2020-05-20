import collections


def maxSubArray(nums):
    highestSum = 0
    currentSum = 0
    # First number in subArray. If currentSum goes below this number, cut off and start a new subArray.
    initialNumber = 0
    count = 0

    while count < len(nums):  # Go through the given array
        # Initialize for inital case
        if count == 0:
            currentSum += nums[count]  # -2
            # print("count:", count, currentSum, ":currentSum")
            initialNumber = nums[count]  # -2
            # print("InitialNumber:", initialNumber)
            count += 1

        else:
            if currentSum == 0:
                initialNumber = nums[count]

            newSum = currentSum + nums[count]
            # if newSum > 0:
            #     print("newSum: ", newSum, count,
            #       ":count", "initalNumber", initialNumber)
            # else:
            #     print("newSum:", newSum, count, ":count",
            #       "initalNumber", initialNumber)

            if count > 0 and newSum > initialNumber:
                currentSum += nums[count]
                # print("Line27:", count, currentSum)
                count += 1

            if newSum <= initialNumber:
                if currentSum >= highestSum:
                    # print("Reset")
                    highestSum = currentSum
                    currentSum = 0
                    initialNumber = nums[count]
                    if count < len(nums):
                        count += 1

                else:
                    # print("here")
                    count += 1

    print(highestSum)


Input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray(Input)
