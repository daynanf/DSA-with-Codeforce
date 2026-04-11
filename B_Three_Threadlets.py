t=int(input())
while t:
    t-=1
    nums=list(map(int,input().split()))
    nM=min(nums)
    nMX=max(nums)
    s=sum(nums)
    m=s-nM-nMX
    if nM == nMX:
        print("YES")
        continue
    ans=(nMX-nM)/nM + (m-nM)/nM
    if ans>3:
        print("NO")
        continue
    elif ans <=3 :        
        print("YES")
        continue
