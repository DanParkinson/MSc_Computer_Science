
arr = [1701,3768]

def Greatest_Common_Denominaotr(arr):
    # Order the numbers

    if arr[0] < arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    
    x = arr[0]
    y = arr[1]

    while x % y != 0:
        print(x, y)
        x, y = y, x% y
    
    print(y)

if __name__ == "__main__":
    Greatest_Common_Denominaotr(arr)
        