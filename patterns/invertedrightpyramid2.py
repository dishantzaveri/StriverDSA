class Solution:
    def pattern6(self, N):
        for i in range(1,N+1):
            for j in range(N+1,i, -1):
                print(N+1-j+1, end =" ")
            print()
            
sol = Solution()
N=9
sol.pattern6(N)