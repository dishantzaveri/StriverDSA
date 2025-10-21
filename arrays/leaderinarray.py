def printLeaders(arr, n):
    ans = []
    maxi=arr[n-1]
    ans.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if arr[i]>maxi:
            ans.append(arr[i])
            maxi=arr[i]
    return ans

if __name__== '__main__':
    n=6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeaders(arr, n)

    print(ans)

    print()    