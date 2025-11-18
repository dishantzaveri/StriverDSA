class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ans=[]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return ''.join(ans)
            ans.append(first[i])
        return ''.join(ans)
    
if __name__ == "__main__":
    solution=Solution()
    input_strs = ["fintedrview", "internet", "internal", "interval"]
    result = solution.longestCommonPrefix(input_strs)
    print("Longest Common Prefix:", result)  