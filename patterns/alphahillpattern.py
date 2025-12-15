def pattern17(n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        ch=ord('A')
        bp = (2*i+1)//2
        for j in range(1,2*i+2):
            print(chr(ch), end="")
            if j<=bp:
                ch+=1
            else:
                ch-=1
        print(" "*(n-i-1))

pattern17(8)
    