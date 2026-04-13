t=int(input())
while t:
    t-=1
    n=int(input())
    nums=list(map(int,input().split()))
    numsS=set(nums)
    if len(nums)!=len(numsS):
        print(-1)
        continue
    else:
        nums.sort(reverse=True)
        print(*nums)