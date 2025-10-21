def LongestSubseq(a):
    n=len(a)
    if n==0:
        return 0
    longest=1
    st=set()
    for i in range(n):
        st.add(a[i])
    for it in st:
        cnt=1
        x=it
        while x+1 in st:
            x+=1
            cnt+=1
        longest=max(longest,cnt)
    return longest

a=[1,2,3,4,5,6,6,6,6,7.1,8,10,0,1002,1001,1002,1003]
ans=LongestSubseq(a)
print(ans)