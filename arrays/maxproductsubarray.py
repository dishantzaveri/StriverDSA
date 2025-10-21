def maxProductSubArray(arr):
    n = len(arr) # size of array.
    pre,suf=1,1
    ans=float('-inf')
    for i in range(n):
        if pre==0:
            pre=1
        if suf==0:
            suf=1
        pre*=arr[i]
        suf*=arr[n-i-1]
        ans=max(ans,max(pre,suf))
    return ans
    
    
    
    
    
    
arr = [1, 120, -3, 0, -4, -125]
print("The maximum product subarray is:", maxProductSubArray(arr))