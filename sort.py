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


def quick(nums):
    raise NotImplementedError

def merge(nums):
    raise NotImplementedError

def bubble(nums):
    raise NotImplementedError