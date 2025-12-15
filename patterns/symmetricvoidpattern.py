def pattern19(n):
    s=0
    for i in range(n):
        print("*" * (n-i), end="")
        print(" " * s, end="")
        print("*" * (n-i))
        s+=2
    s=2*n-2
    for i in range(1,n+1):
        print("*" * (i), end="")
        print(" " * s, end="")
        print("*" * (i))
        s-=2   

pattern19(6)    
        