# class Solution:
#     def pattern10(self, N):
#         for i in range(1, N + 1):
#             print("* " * (2*i - 1))
#         for i in range(N - 1, 0, -1):
#             print("* " * (2*i - 1))

# if __name__ == "__main__":
#     sol = Solution()
#     sol.pattern10(5)

                                                    #OR


def pattern10(N):
    for i in range(1, 2*N):
        stars = i
        if i > N:
            stars = 2*N - i
        print("*" * stars)

if __name__ == "__main__":
    N = 5
    pattern10(N)

