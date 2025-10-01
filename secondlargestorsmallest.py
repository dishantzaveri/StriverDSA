def secondLargest(arr, n):
        if (n < 2):
            return -1
        large = 1
        second_large = -1
        for i in range(n):
            if (arr[i] > large):
                second_large = large
                large = arr[i]
            elif (arr[i] > second_large and arr[i] != large):
                second_large = arr[i]
        return second_large

def secondSmallest(arr,n):
    if (n<2):
        return -1
    small = float('inf')
    s_small = float('inf')
    for i in range(n):
        if (arr[i]<small):
            s_small=small
            small = arr[i]
        elif (arr[i]<s_small and arr[i] != small):
            s_small=arr[i]
    return s_small

if __name__ == "__main__":
    arr=[1,-100,-2,234,0]
    n=len(arr)
    sS = secondSmallest(arr,n)
    print(sS)
    sL = secondLargest(arr,n)
    print(sL)