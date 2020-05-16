# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

import time
from Array_test import A
from BinarySearchTree import BinarySearchTree


def containsDuplicates(nums):
    NewObj = {}

    for i in range(0, len(nums)):
        if nums[i] in NewObj.keys():
            print("Duplicate")
            return True
        else:
            NewObj[nums[i]] = [i]

    print("No Duplicates")
    return False


def containsBST(nums):

    pass

    # bst_nums = BinarySearchTree(nums[0])
    # for num in nums:
    #     bst_nums.insert(num)

    # for number in nums:
    #     if bst_nums.contains(number):
    #         return True


start_time = time.time()
containsDuplicates(A)
end_time = time.time()
total_time = end_time - start_time
print("One", total_time)


start_time = time.time()
containsBST(A)
end_time = time.time()
total_time = end_time - start_time
print("Contains", total_time)
