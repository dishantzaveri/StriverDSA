def pattern18(n):
    for i in range(n):
        start=ord('A') +n -1 -i
        end=ord('A')+n-1
        for ch in range(start, end +1):
            print(chr(ch), end=" ")
        print()
        
pattern18(5)