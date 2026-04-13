t=int(input())
while t:
    t-=1
    x ,m=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    modes=[(nums[i]+i)%m for i in range(len(nums))]
    m=min(modes)
    mx=max(modes)
    if m==0:
        if modes.count(m)==x:
            print("YES")
        else:
            
