class Solution:
    def nextGreater(self, nums):
        stack = []
        n = len(nums)
        res = [0] *n
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                res[i] =-1
            else:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res
    
def main():
    nums = [4, 5, 2, 10]
    sol = Solution()
    ans = sol.nextGreater(nums)
    print(" ".join(map(str, ans)))

main()