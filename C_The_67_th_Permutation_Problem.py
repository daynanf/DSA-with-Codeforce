t=int(input())
while t:
    t-=1
    n=int(input())
    ans=[]
    b=3*n
    for i in range(1,n+1):
        ans.append(b)
        b-=1
        ans.append(b)
        b-=1
        ans.append(i)
    print(*ans)