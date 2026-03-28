t= int(input())
while t:
    t-=1
    n=int(input())
    s=input()
    prev=""
    cnt=0
    gap=0
    numD=0
    for x in s:
        if x==".":
            numD+=1
        if x=="." and x==prev:
            cnt+=1
        else:
            cnt=0
        gap=max(gap,cnt)
        prev=x
    if gap>=2:
        print(2)
    else:
        print(numD)