# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    if len(arrA) == 1 and len(arrB) == 1:
        if arrA[0] < arrB[0]:
            return [arrA[0], arrB[0]]
        else:
            return [arrB[0], arrA[0]]
    #set counters for left, right, and final merged arrays
    i = 0
    j = 0
    final = 0
    #iterate through left and right
    while i < len(arrA) and j < len(arrB):
        #If i is less than or equal to j
        if arrA[i] <= arrB[j]:
            #assign the next null slot in merge array to element i of arrA
            merged_arr[final] = arrA[i]
            #increment i
            i += 1
        else:
            #assign the next null slot in the merged array to element j of arrB
            merged_arr[final] = arrB[j]
            #increment j
            j += 1
        #increment final
        final += 1

    print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #SPLIT BASE CASE
    if len(arr) < 2:
        print(arr)
        return arr
    #split the current array into left and right
    else:
        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]
        left = merge_sort(left_array)
        right = merge_sort(right_array)
        merged = merge(left, right)
        return merged

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

if __name__ == "__main__":
    print(merge_sort([1, 3, 2, 7, 4, 5, 6]))
    # print(merge([1], [2]))