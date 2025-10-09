
from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) 
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0
    
    mpp[0]=1
    for i in range(n):
        preSum+=arr[i]
        remove=preSum-k
        cnt+=mpp[remove]
        mpp[preSum]+=1
    return cnt

if __name__ == '__main__':
    arr = [3, 1, 2, 4,-2,4,9,-3,-4,-2,-1,5,4,3,2]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)