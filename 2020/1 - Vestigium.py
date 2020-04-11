t = int(input())

trace = 0
rc = 0
cc = 0
mat = []
extra = []
col = -1

for i in range(t):
    n = int(input())
    
    for j in range(n):
        l = list(map(int, input().split()))
        mat.append(l)
    
    for j in range(0, n):
        for k in range(0, n):
            if(j == k):
                trace += mat[j][k]

    for j in range(0, n):
        s = set(mat[j])
        if(len(s) < len(mat[j])):
            rc += 1

    for j in range(n):
        for k in range(0, n):
            extra.append(mat[k][j])

        s1 = set(extra)
        if(len(s1) < len(extra)):
            cc += 1

        extra = []

    print('Case #'+str(i+1)+':', trace, rc, cc)
    trace = 0
    rc = 0
    cc = 0
    mat = []
