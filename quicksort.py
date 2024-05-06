def quicksort(arr):
    if len(arr) < 2:
        return arr  # base case: arrays with 0 or 1 elements are already "sorted"
    else:
        pivot = arr[0] #recursive case
        less = [i for i in arr[1:] if i <= pivot] # sub-array of all the elements less than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
testArr = [10, 5, 2, 3]
print(quicksort(testArr))