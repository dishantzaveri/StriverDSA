def search(arr, n, k):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=k and k<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=k and k<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 8
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
