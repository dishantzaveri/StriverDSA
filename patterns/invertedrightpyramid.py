class Solution:
    def pattern5(self, N):
        for i in range(1,N+1):
            for j in range(N+1,i, -1):
                print("*", end =" ")
            print()
            
sol = Solution()
N=5
sol.pattern5(N)