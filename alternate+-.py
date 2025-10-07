from typing import List

def RearrangebySign(A: List[int]) -> List[int]:
    n = len(A)
    
    ans = [0] * n
    
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2
    
        else:
            ans[posIndex] = A[i]
            posIndex += 2
    
    return ans
    
A = [1,2,-4,-5]
ans = RearrangebySign(A)

print(ans)