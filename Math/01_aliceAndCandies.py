a = int(input())

count = 0

if(a % 2 == 1):
    count += 1

n = (a//2)+2 
for j in range(1, n, 2):
    sum = 0
    for k in range(j,n,2):
        if sum == a:
            count+=1
            break
        elif sum>a:
            break
        sum+=k
print(count)
