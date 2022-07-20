# test all the sorting functions

import argparse
from random import randint
import sort

# parse arguments to see which sort to run
parser = argparse.ArgumentParser()
parser.add_argument("length", help="Number of elements in the array to be sorted", action='count', default=5)
parser.add_argument("-A", help="call All sorting algorithms", action='store_true')
parser.add_argument("-q", help="call Quicksort", action='store_true')
parser.add_argument("-r", help="call Random sort", action='store_true')
args = parser.parse_args()

if args.q or args.A:
    print("#"*20)
    print("Quick sort:")
    print("#"*20)
    for _ in range(1):
        arr = [randint(0, 100) for _ in range(args.length)]
        copy = arr[:]
        print("Input arr:", copy)
        arr = sort.quick(arr)
        print("Array after sort:", arr)
        assert(arr == sorted(copy))

if args.r or args.A:
    print("#"*20)
    print("Random sort:")
    print("#"*20)
    for _ in range(1):
        arr = [randint(0, 100) for _ in range(args.length)]
        copy = arr[:]
        print("Input arr:", copy)
        sort.rand(arr)
        print("Array after sort:", arr)
        assert(arr == sorted(copy))