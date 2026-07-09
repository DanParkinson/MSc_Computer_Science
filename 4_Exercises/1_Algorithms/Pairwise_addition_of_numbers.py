
arr = [ 1,2,3]

def pairiwse_sum(arr):
    print(arr)

    while len(arr) > 1:

        new_arr = []

        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):
                new_arr.append(arr[i] + arr[i + 1])
            else:
                new_arr.append(arr[i])

        arr = new_arr
        print(arr)

if __name__ == "__main__":
    pairiwse_sum(arr)
        