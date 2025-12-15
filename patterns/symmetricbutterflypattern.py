def pattern20(n):
    spaces=2*n-2
    for i in range(1,2*n):
        stars = i if i<=n else 2*n-i
        print("*"*stars + " " * spaces + "*" * stars)
        spaces-=2 if i <n else -2

pattern20(5)