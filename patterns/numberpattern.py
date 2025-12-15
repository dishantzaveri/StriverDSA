def pattern22(n):
    size = 2*n-1
    for i in range(size):
        for j in range(size):
            top=i 
            left=j
            bottom = size - 1 -i
            right = size - 1 - j 
            m = min(top,left,bottom,right)
            print(n-m, end = " ")
        print()

pattern22(9)