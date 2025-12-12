class Solution:
    def pattern4(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(i, end=" ")
            print()
            
sol = Solution()
N=5
sol.pattern4(N)