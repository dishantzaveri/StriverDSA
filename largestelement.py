def findlargestnumber(arr,n):
    max = arr[0]
    for i in range(n):
        if (max<arr[i]):
            max=arr[i]
    return max

if __name__ == "__main__":
    arr1=[1,2,3,2,4233,7]
    n=6
    max1 = findlargestnumber(arr1,n)
    print(max1)
    