class Solution:
    def pattern7(self, N):
        for i in range(N):
            for j in range(N-i -1):
                print("   ", end ="")
            for j in range(2*i+1):
                print(" * ", end ="")
            for j in range(N-i -1):
                print("   ", end ="")
            print()
            
sol = Solution()
N=5
sol.pattern7(N)