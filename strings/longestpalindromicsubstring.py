#without dp

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for center in range(len(s)):
            len1 = self.expandFromCenter(s, center, center)
            len2 = self.expandFromCenter(s, center, center + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = center - (max_len - 1) // 2
                end = center + max_len // 2
        return s[start:end + 1]

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

if __name__ == "__main__":
    sol = Solution()
    input_str = "babababababababbabbbaabbabababbabad"
    print("Longest Palindromic Substring:", sol.longestPalindrome(input_str))