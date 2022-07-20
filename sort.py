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


def merge(nums):
    raise NotImplementedError

def bubble(nums):
    raise NotImplementedError
