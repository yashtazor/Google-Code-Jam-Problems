t = int(input())

for i in range(t):
    
    bracks = []
    ans = ''
    lb = 0
    rb = 0
    s = input()
    l = list(s)    

    for j in range(1, len(l)):
        if(int(l[j-1]) >= int(l[j])):
            brac = int(l[j-1]) - int(l[j])
            bracks.append(')'*brac)
        else:
            brac = int(l[j]) - int(l[j-1])
            bracks.append('('*brac)

    bracks = ['('*int(s[0])] + bracks

    for j in range(0, len(s)):
        x = bracks[j] + l[j]
        ans += x

    for j in ans:
        if(j == '('):
            lb += 1
        elif(j == ')'):
            rb += 1
        else:
            continue

    brac = lb - rb

    ans = ans + ')'*brac

    print('Case #'+str(i+1)+':', ans)
    

    






        
