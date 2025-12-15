def pattern12(n):
    spaces = 2*(n-1)
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end ="")
        print(" " * spaces, end = "")
        for j in range(i,0,-1):
            print(j, end ="")
        print()
        spaces-=2
pattern12(7)
    