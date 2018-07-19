import re
def move (s):
    s = list(re.split('[ ]+',s))
    n = len(s)
    i = n-1
    c = 0
    while(i):
        if s[i] == s[i-1]:      
            del s[i-1]
            c = c + 1
        i = i-1

    for j in range(0,n-c):
        print(s[j])
s = input()
move(s)