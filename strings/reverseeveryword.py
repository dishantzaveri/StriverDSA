class Solution:
    def reverseString(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        self.reverseString(s, 0, n - 1)

        i = 0
        j = 0
        start = 0
        end = 0

        while j < n:
            while j < n and s[j] == ' ':
                j += 1
            if j == n:
                break

            start = i

            while j < n and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1

            end = i - 1

            self.reverseString(s, start, end)

            if j < n:
                s[i] = ' '
                i += 1

        if i > 0 and s[i - 1] == ' ':
            i -= 1

        return "".join(s[:i])


if __name__ == "__main__":
    s = " amazing coding skills "
    sol = Solution()
    ans = sol.reverseWords(s)
    print("Input string:", s)
    print("After reversing every word:", ans)