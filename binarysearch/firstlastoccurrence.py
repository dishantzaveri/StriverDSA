class Solution:
    def searchRange(self, nums, target):
        def first():
            l, r, ans = 0, len(nums) - 1, -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    if nums[m] == target:
                        ans = m
                    r = m - 1
                else:
                    l = m + 1
            return ans
        def last():
            l, r, ans = 0, len(nums) - 1, -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    if nums[m] == target:
                        ans = m
                    l = m + 1
                else:
                    r = m - 1
            return ans
        return [first(), last()]

if __name__ == "__main__":
    tests = [
        ([5,7,7,8,8,10], 8),
        ([5,7,7,8,8,10], 6),
        ([], 0),
        ([1,1,1,1], 1),
        ([1,2,3,4,5], 3),
        ([2,2,2,3,3,4,5,5,6], 2),
    ]
    s = Solution()
    for nums, target in tests:
        print(nums, target, "->", s.searchRange(nums, target))
