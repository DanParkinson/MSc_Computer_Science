
arr = [1, 6,5,4,3,2]

def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(arr)
    





if __name__ == "__main__":
    bubble_sort(arr)