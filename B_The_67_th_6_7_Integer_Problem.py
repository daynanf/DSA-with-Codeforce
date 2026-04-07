t=int(input())
while t:
    t-=1
    nums=list(map(int,input().split()))
    s=sum(nums)
    m=max(nums)
    ans=2*m-s
    print(ans)