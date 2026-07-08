'''
Selection Sort

Premise:
Take an unordered list, compare its value with all values int the array. insert smallest value at current index

Time:
- Quadratic running time O(n)^2
- Takes the same amount of time regardless of how sorted the data is

PSEUDO:
For ecah index in array:
    set current index as minimum
    For other indexes:
        if current index smaller:
            set smallest index to current
    swap values or current index and smallest index
'''

arr = [2, 6, 5, 1, 3, 4]

def selection_sort(arr):
    for i in range( 0, len(arr) -1):                                # go through each index of the arry
        current_min_ind = i                                         # set the current index as the smallest
        for j in range(i+1, len(arr)):                              # Go through all other indexes
            if arr[j] < arr[current_min_ind]:                       # compare current index in second loop with current minimum index
                current_min_ind = j                                 # if smaller, set it as new minimum
        arr[i], arr[current_min_ind] = arr[current_min_ind], arr[i] # swap the current index in the array with the smallest
        print(arr)
    
    print(arr)

if __name__ == "__main__":
    selection_sort(arr)
    