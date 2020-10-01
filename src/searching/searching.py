def linear_search(arr, target):
    # Your code here
    for a in arr:
        if a == target:
            return arr.index(a)


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    high = len(arr)-1
    low = 0
    while low <= high:
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid

        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # not found
