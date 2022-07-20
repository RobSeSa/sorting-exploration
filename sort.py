# all of the sorting functions
import random

def is_sorted(nums):
    if len(nums) <= 1:
        return True
        
    for i, num in enumerate(nums[:len(nums)-1]):
        if not num <= nums[i+1]:
            return False
    return True

###################
### Random Sort ###
###################
def rand(nums):
    # randomly do swaps until nums is sorted
    while not is_sorted(nums):
        random.shuffle(nums)
    return

##################
### Quick Sort ###
##################
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

##################
### Merge Sort ###
##################
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

#######################
### Insertion Sort ###
#######################
def insertion(nums):
    '''
    find the lowest elem n times and move it to the front

    find lowest O(n)
    swap to front O(1)
    repeat n times O(n)
    '''
    for i in range(0,len(nums)):
        # find lowest
        lowest = nums[i]
        lowest_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < lowest:
                lowest = nums[j]
                lowest_index = j
        # swap to front
        nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
    return nums


###################
### Bucket Sort ###
###################
def bucket(nums, n):
    max_val = max(nums) + 0.000001
    nums = [num / max_val for num in nums]
    arr = []
    
    for _ in range(n):
        arr.append([]) # create array of n buckets (lists)

    # Put array elements in different buckets 
    for j in nums:
        index_b = int(n * j) 
        arr[index_b].append(j)
      
    # Sort individual buckets 
    for i in range(n):
        arr[i] = insertion(arr[i])
          
    # concatenate the result
    k = 0
    for i in range(n):
        for j in range(len(arr[i])):
            nums[k] = arr[i][j]
            k += 1
    
    nums = [int(round(num * max_val)) for num in nums]
    return nums