def pattern21(n):
    for i in range(n):
        for j in range(n):
            print("*" if i == 0 or j ==0 or i ==n-1 or j==n-1 else " ", end="")
        print()
        
pattern21(7)