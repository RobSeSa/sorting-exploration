# test all the sorting functions

import argparse
from random import randint
import sort

# parse arguments to see which sort to run
parser = argparse.ArgumentParser("simple_example")
parser.add_argument("length", help="Number of elements in the array to be sorted", type=int)
args = parser.parse_args()
print(args.length + 1)


for _ in range(1):
    arr = [randint(0, 100) for _ in range(args.length)]
    copy = arr[:]
    print("Input arr:", copy)
    sort.rand(arr)
    print("Array after sort:", arr)
    assert(arr == sorted(copy))