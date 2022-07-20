# all of the sorting functions
import random

def is_sorted(nums):
    if len(nums) <= 1:
        return True
        
    for i, num in enumerate(nums[:len(nums)-1]):
        if not num <= nums[i+1]:
            return False
    return True



def rand(nums):
    # randomly do swaps until nums is sorted
    while not is_sorted(nums):
        random.shuffle(nums)
    return

def bucket(nums):
    raise NotImplementedError

### Quick Sort ###
def quick(nums):
    less = []
    equal = []
    greater = []
    if len(nums) <= 1:
        return nums
    pivot_index = random.randint(0, len(nums)-1)
    pivot = nums[pivot_index]
    for i, num in enumerate(nums):
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            less.append(num)
        else:
            greater.append(num)
    return quick(less) + equal + quick(greater)

### Merge Sort ###
def merge(nums1, nums2):
    # nums1 and nums2 must be sorted
    i1, i2 = 0, 0
    res = []
    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] < nums2[i2]:
            res.append(nums1[i1])
            i1 += 1
        else:
            res.append(nums2[i2])
            i2 += 1
    if i1 < len(nums1):
        res.extend(nums1)
    elif i2 < len(nums2):
        res.extend(nums2)
    return res

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    elif len(nums) == 2:
        return nums if nums[0] < nums[1] else [nums[1], nums[0]]
    
    left = merge_sort(nums[:len(nums)//2])
    right = merge_sort(nums[len(nums)//2:])
    return merge(left, right)
    


def bubble(nums):
    raise NotImplementedError
