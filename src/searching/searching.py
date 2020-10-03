# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #before base case, set start and end at start and end of array
    #these will narrow as we recurse
    midpoint_index = (start + end) // 2
    #BASE CASE
    #if the midpoint is the target, return the target
    if arr[midpoint_index] == target:
        return target
    #RECURSIVE CASES
    #if the midpoint is less than the target, recurse on the right half
    if arr[midpoint_index] < target:
        binary_search(arr, target, midpoint_index, end)
    #if the midpoint is greater than the target, recurse on the left half
    if arr[midpoint_index] > target:
        binary_search(arr, target, start, midpoint_index)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

