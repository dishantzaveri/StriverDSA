class Solution:
      def isomorphicString(self, s, t):
          m1,m2=[0]*256,[0]*256
          n=len(s)
          for i in range(n):
              if m1[ord(s[i])] !=m2[ord(t[i])]:
                  return False
              m1[ord(s[i])]=i+1
              m2[ord(t[i])]=i+1
              
          return True
  
if __name__ == "__main__":
      solution = Solution()
      s = "paper"
      t = "title"
      if solution.isomorphicString(s, t):
          print("Strings are isomorphic.")
      else:
          print("Strings are not isomorphic.")