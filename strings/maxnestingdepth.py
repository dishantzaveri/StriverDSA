class Solution:
    def maxDepth(self, s: str) -> int:
        p=0
        ans=0
        for ch in s:
            if ch=="(":
                p+=1
            elif ch==')':
                p-=1
            ans=max(ans,p)
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    s = "(1+(2*3)+((8+((((((8)))))))/4))+1"
    result = sol.maxDepth(s)
    print("Max Depth:", result)