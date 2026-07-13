

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def binary_search(arr, value):

    min = 0
    max = len(arr) -1

    while min <= max:
        midpoint = (max + min) // 2
        print(f"Searching in range: {min} - {max}")

        if arr[midpoint] == value:
            print(f"{value} is at index: {midpoint}")
            return midpoint
        elif value > arr[midpoint]:
            min = midpoint + 1
        else:
            max = midpoint - 1
    
    print(f"{value} was not found.")
    return -1

if __name__ == "__main__":
    binary_search(arr, 15)





