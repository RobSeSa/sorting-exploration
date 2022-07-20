# test all the sorting functions

from random import randint
import sort


for _ in range(1):
    arr = [randint(0, 100) for _ in range(5)]
    copy = arr[:]
    print("Input arr:", copy)
    sort.rand(arr)
    print("Array after sort:", arr)
    assert(arr == sorted(copy))