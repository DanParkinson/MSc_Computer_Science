'''
Insertion Sort

Premise:
compare current value with next until next is smaller
if smaller swap
go backwards until correctly placed
go back to first swap in this pass and repeat

Time:
very good with nearly sorted data
Time complexity is O(n)^2 as worst case

PSEUDO

Define array

for index in array
    for next index in array
        if value current smaller than value next
            swap
        
'''

arr = [2, 6, 5, 1, 3, 4]

def insertion_sort(arr):
    for i in range(1, len(arr)):                  # Each unsorted value
        value_to_sort = arr[i]                    # Remember the value to sort
        while arr[i-1] > value_to_sort and i > 0: # If the previous value is bigger and its not the first pass
            arr[i], arr[i-1] = arr[i-1], arr[i]   # swap current value with the bigger previous value
            print(arr)
            i = i -1                              # once swapped, go back to the start until all values are in order
    print(arr)

if __name__ == "__main__":
    insertion_sort(arr)

            


