t=int(input())
while t:
    t-=1
    s,n=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    if n in nums:
        print("YES")
    else:
        print("NO")