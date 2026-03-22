t=int(input())
while t:
    t-=1
    x=int(input())
    cnt=0
    y=x%15
    n=x//15
    for i in range(y+1):
        if i%3 == i%5:
            cnt+=1
    ans=3*n+cnt
    print(ans)