# test all the sorting functions

import argparse
from random import randint
import sort

# parse arguments to see which sort to run
parser = argparse.ArgumentParser()
parser.add_argument("length", help="Number of elements in the array to be sorted", action='count', default=4)
parser.add_argument("iter", help="Number of times to repeat sorting algo", action='count', default=0)
parser.add_argument("-A", help="call All sorting algorithms", action='store_true')
parser.add_argument("-q", help="call Quicksort", action='store_true')
parser.add_argument("-m", help="call Merge sort", action='store_true')
parser.add_argument("-r", help="call Random sort", action='store_true')
args = parser.parse_args()
print(args)

if args.m or args.A:
    print("#"*20)
    print("Merge sort:")
    print("#"*20)
    for _ in range(args.iter):
        arr = [randint(0, 100) for _ in range(args.length)]
        copy = arr[:]
        print("Input arr:", copy)
        arr = sort.quick(arr)
        print("Array after sort:", arr)
        assert(arr == sorted(copy))

if args.q or args.A:
    print("#"*20)
    print("Quick sort:")
    print("#"*20)
    for _ in range(args.iter):
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
    for _ in range(args.iter):
        arr = [randint(0, 100) for _ in range(args.length)]
        copy = arr[:]
        print("Input arr:", copy)
        sort.rand(arr)
        print("Array after sort:", arr)
        assert(arr == sorted(copy))