# selection-sort
# bigO(n^2)

def findSmallest(arr):
    smallest = arr[0]           # stores the smallest value
    smallest_index = 0          # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): # this sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)        # finds the smallest element in the array,
        newArr.append(arr.pop(smallest))    # and add it to the new array
    return newArr

testArray = [5,3,6,2,10]
print(selectionSort(testArray))