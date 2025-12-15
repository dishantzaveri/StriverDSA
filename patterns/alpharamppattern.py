def pattern16(n):
    for i in range(n):
        ch = chr(ord('A')+i)
        for _ in range(i+1):
            print(ch,end=" ")
        print()
pattern16(26)
        