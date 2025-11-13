class Solution:

    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

nums = [4, 5, 6, 1, 2, 3]

sol = Solution()

result = sol.findMin(nums)

print("Minimum element is", result)