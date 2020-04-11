t = int(input())

for i in range(t):
    n = int(input())

    tasks = []
    temp = []
    flag = 0
    start = "C"

    for j in range(n):
        l = tuple(map(int, input().split()))
        tasks.append(l)


    for j in range(0, len(tasks)-2):
        if((tasks[j][0] <= tasks[j+1][0]) and (tasks[j][1] >= tasks[j+1][1])):
            if((tasks[j+1][0] <= tasks[j+2][0]) and (tasks[j+1][1] > tasks[j+2][0])):
                flag = 1
                break

    if(flag == 1):
        ans = "IMPOSSIBLE"
    else:
        for j in range(1, len(tasks)):
            if((tasks[j-1][0] < tasks[j][1] and tasks[j-1][1] > tasks[j][0]) or (tasks[j-1][0] <= tasks[j][0] and tasks[j-1][1] >= tasks[j][1])):
                if(start[-1] == 'J'):
                    start += "C"
                else:
                    start += "J"
            else:
                if(tasks[j-1][1] == tasks[j][0]):
                    if(start[-1] == 'J'):
                        start += "J"
                    else:
                        start += "C"

                for k in range(j, -1, -1):
                    if(tasks[j][0] == tasks[k][1]):
                        if(start[-1] == 'J'):
                            start += "J"
                        else:
                            start += "C"

            ans = start
    print('Case #'+str(i+1)+':', ans)

    
        
