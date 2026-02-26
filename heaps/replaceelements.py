class Solution:
    def replaceWithRank(self, arr):
        sorted_arr = sorted(arr)
        rank_map = {}
        rank = 1
        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1
        result = [rank_map[num] for num in arr]
        return result

obj = Solution()
arr = [1, 5, 8, 15, 8, 25, 9]
res = obj.replaceWithRank(arr)
print(*res)