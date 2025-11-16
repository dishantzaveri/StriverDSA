def reverseWords(s: str) -> str:
    n = len(s)
    i = n - 1
    res = ''
    
    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            break
        j = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        word = s[i+1:j+1]
        if res:
            res += ' '
        res += word
    return res