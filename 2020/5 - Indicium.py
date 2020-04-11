t = int(input())

for a in range(t):
    n, k = map(int, input().split())

    b = n + 1
    row = []
    mat = []
    ans = []
    flag = 0

    trace = 0

    for i in range(1, n + 1, 1):  

        temp = b  
        while (temp <= n) : 
            temp += 1
            row.append(temp-1)

        for j in range(1, b): 
            row.append(j)
      
        b -= 1

        mat.append(row)
        row = []

    for i in range(n):
        l = mat[n-1]

        for j in range(n - 1, 0, -1): 
            mat[j] = mat[j - 1]; 
              
        mat[0] = l;

        for p in range(0, n):
            for q in range(0, n):
                if(p == q):
                    trace += mat[p][q]
    
        if(trace == k):
            ans = mat
            flag = 1
            break
        else:
            flag = 0

        trace = 0

    if(flag == 1):
        print('Case #'+str(a+1)+':', "POSSIBLE")
        for i in range(0, len(ans)):
            for j in range(0, len(ans[i])):
                print(ans[i][j], ' ', end='')
            print()
                           
    else:
        print('Case #'+str(a+1)+':', "IMPOSSIBLE")
     
