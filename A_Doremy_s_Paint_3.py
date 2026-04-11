t=int(input())
while t:
    t-=1
    n=int(input())
    nums=list(map(int,input().split()))
    numsSet=set(nums)
    if len(numsSet)<=1:
        print("YES")
    elif len(numsSet)==2:
        from collections import Counter
        freq = Counter(nums)
        a,b=freq.values()
        if a==b or abs(a-b)==1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")