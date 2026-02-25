import heapq

class Solution:
    def kls(self,nums,k):
        pq = []
        for i in range(k):
            heapq.heappush(pq,nums[i])
        for i in range(k, len(nums)):
            if nums[i]>pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq,nums[i])
        return pq[0]
    
    
def main():
    nums = [-5,4,1,2,-3]
    k = 5
    sol = Solution()
    ans = sol.kls(nums,k)
    print("The Kth largest element in the array is:", ans)

if __name__ == "__main__":
    main() 