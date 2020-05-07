# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
import time
from Array_test import A


def ReturnIndices(nums, target):
    total = 0

    current_index = 0
    limit = len(nums)-1
    while current_index != limit:
        for i in range(current_index+1, len(nums)):
            if current_index == i:
                pass
            else:
                total = nums[current_index] + nums[i]
                if total == target:
                    print([current_index, i])
                    return [current_index, i]
        current_index += 1


def ReturnIndicesNew(nums, target):
    total = 0

    current_index = 0
    limit = len(nums)-1
    for outer_value in nums[0:limit]:
        i = current_index + 1
        counter = i
        for value in nums[counter:]:
            total = outer_value + value
            if total == target:
                print([current_index, counter])
                return [current_index, counter]
            counter += 1
        current_index += 1


def ReturnIndicesObj(nums, target):
    NewObj = {}

    for i in range(0, len(nums)):
        if nums[i] in NewObj.keys():
            NewObj[nums[i]].append(i)
        else:
            NewObj[nums[i]] = [i]

    for keys in NewObj.keys():
        ST = target - keys
        if ST in NewObj.keys():
            if ST == keys and len(NewObj[ST]) > 1:
                print(NewObj[ST])
                return NewObj[ST]
            else:
                arr = []
                arr.append(NewObj[keys][0])
                arr.append(NewObj[ST][0])
                print(arr)
                return (arr)


def ReturnIndicesObjOnePass(nums, target):
    NewObj = {}

    for i in range(0, len(nums)):
        if nums[i] in NewObj.keys():
            NewObj[nums[i]].append(i)
            ST = target - nums[i]
        else:
            NewObj[nums[i]] = [i]
            ST = target - nums[i]
            if ST in NewObj.keys():
                arr = []
                arr.append(NewObj[nums[i]][0])
                arr.append(NewObj[ST][0])
                print(arr)
                return (arr)


# start_time = time.time()
# # ReturnIndicesNew([0, 4, 3, 0], 0)
# ReturnIndices(A, 16021)
# end_time = time.time()
# total_time = end_time - start_time
# print("Old", total_time)

# start_time = time.time()
# # ReturnIndicesNew([0, 4, 3, 0], 0)
# ReturnIndicesNew(A, 16021)
# end_time = time.time()
# total_time = end_time - start_time
# print("New", total_time)

start_time = time.time()
ReturnIndicesObj([0, 4, 3, 0], 0)
# ReturnIndicesNew(A, 16021)
end_time = time.time()
total_time = end_time - start_time
print("Obj", total_time)

start_time = time.time()
ReturnIndicesObjOnePass([0, 4, 3, 0], 0)
# ReturnIndicesObjOnePass(A, 16021)
end_time = time.time()
total_time = end_time - start_time
print("Obj OnePass", total_time)
