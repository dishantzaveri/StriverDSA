class Solution:
    def nthRoot(self, n, m):
        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    break
            if ans == m:
                return mid
            if ans < m:
                low = mid + 1
            else:
                high = mid - 1

        return -1

obj = Solution()
result = obj.nthRoot(3, 27.9)
print(result)