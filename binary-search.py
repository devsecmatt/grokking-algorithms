# binary search
# using a sorted list of elements, and you are searching for an element in that list, 
# binary search returns the position where it is located

def binary_search(list, item):
    low = 0 #low and high keep track of which part of the search you are in
    high = len(list)-1

    while low <= high:  # while not narrowed down to a single search element
        mid = (low+high)//2 # check the middle element
        guess = list[mid]
        if guess == item:   # if the item is found
            return mid
        elif guess > item:    # the guess was too high
            high = mid - 1
        else:               # the guess was too low
            low = mid + 1
    return None             # the item doesn't exist

print("binary search")
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None

# Big O notation - O(n) - worst case scenario
# Binary search  - logarithmic time O(log n)
# Simple search - linear time O(n) 
