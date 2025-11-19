class Solution:
    def myAtoi(self, s:str) -> int:
        i=0
        sign=1
        res=0
        while i<len(s) and s[i] == ' ':
            i+=1
        if i==len(s):
            return 0
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1
        while i<len(s) and s[i].isdigit():
            res=res*10+int(s[i])
            if sign*res>2**31-1:
                return 2**31 -1
            if sign*res<-2**31:
                return -2**31
            i+=1
            
        return sign*res

if __name__ == "__main__":
    sol = Solution()
    input_str = " 400909909909042"
    result = sol.myAtoi(input_str)
    print("Converted integer:", result)