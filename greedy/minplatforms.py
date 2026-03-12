class Solution:
    def countPlatforms(self,arr,dep,n):
        arr.sort()
        dep.sort()
        platforms = 1
        result = 1
        i,j =1,0
        while i < n and j<n:
            if arr[i] <=dep[j]:
                platforms+=1
                i+=1
            else:
                platforms -=1
                j+=1
            result = max(result, platforms)
        return result
    
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = len(arr)

obj = Solution()
print("Minimum number of Platforms required",
      obj.countPlatforms(arr, dep, n))
    