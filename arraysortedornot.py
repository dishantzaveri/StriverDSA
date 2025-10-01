def isSorted(arr, n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 4, 3, 5]
    n = 5
    print("True" if isSorted(arr, n) else "False")