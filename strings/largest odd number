def largestOdd(s:str) -> str:
    last_odd=-1
    for i in range(len(s)-1,-1,-1):
        if s[i] in '13579':
            last_odd=i
            break
    if last_odd==-1:
        return ""
    start=0
    while start<last_odd and s[start]=='0':
        start+=1
    return s[start:last_odd+1]
            