def merge(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    pointer1 = 0
    pointer2 = 0
    lastZero = len(nums1) - len(nums2) -1
    
    while pointer2 < len(nums2) and pointer1 < len(nums1):
        a = nums1[pointer1]
        b = nums2[pointer2]
        
        if a == 0 and pointer1 > lastZero:
            nums1[pointer1] = b
            pointer1 += 1
            pointer2 += 1
        elif a <= b:
            pointer1 += 1
        elif a > b:
            c = a
            nums1[pointer1] = b
            nums2[pointer2] = c
            nums2 = sorted(nums2)
            pointer1 += 1