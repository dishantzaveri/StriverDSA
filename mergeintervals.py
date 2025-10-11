from typing import List

def mergeIntervals(arr: List[List[int]]) -> List[List[int]]:
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n):
        if not ans or arr[i][0]>ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1]=max(ans[-1][1],arr[i][1])
    return ans
        
        
if __name__ == '__main__':
    arr = [[1, 3], [0, 1.3], [2, 100], [15, 18]]
    ans = mergeIntervals(arr)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()