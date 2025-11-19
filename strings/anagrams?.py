def check_anagrams(str1, str2):
    if len(str1)!= len(str2):
        return False
    freq=[0]*26
    for ch in str1:
        freq[ord(ch)-ord('A')] +=1
    for ch in str2:
        freq[ord(ch)-ord('A')] -=1
    for x in freq:
        if x!=0:
            return False
    return True
        
if __name__ == "__main__":
    s1 = "INTEGER"
    s2 = "TEGERNI"
    print("True" if check_anagrams(s1, s2) else "False")