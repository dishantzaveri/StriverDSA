def upperBound(arr: [int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n
    
    while low<=high:
        mid = (low+high) //2
        if arr[mid]>x:
            ans = mid
            high = mid -1
        else:
            low=mid+1

    return ans

if __name__ == "__main__":
    arr = [3, 5, 8,9, 15, 19]
    n = 5
    x = 9
    ind = upperBound(arr, n, x)
    print("The upper bound is the index:", ind)
