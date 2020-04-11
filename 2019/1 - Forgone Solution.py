n = int(input())

case = 0

l = []

for i in range(n):
    item = int(input())
    l.append(item)
    
for i in l:
    for j in range(1, i+1):
        x = j
        y = i - j
        
        lx = [int(a) for a in str(x)]
        ly = [int(b) for b in str(y)]
        
        if((4 in lx) or (4 in ly)):
            continue        
        else:
            case += 1
            print ('Case #'+str(case)+':', x, y)
            break
