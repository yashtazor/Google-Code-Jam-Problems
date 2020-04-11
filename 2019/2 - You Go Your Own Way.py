n = int(input())

cn = 0

s = []
p = []

for i in range(n):
    size = int(input())
    path = str(input())
    s.append(size)
    p.append(path)
    
ans = ""
    
for i in range(0, len(s)):
    for j in range(0, (2*s[i]-2)):
        if(p[i][j] == 'E'):
            ans += 'S'
        else:
            ans += 'E'

    cn += 1        
    print('Case #'+str(cn)+':',ans)
    ans = ""
