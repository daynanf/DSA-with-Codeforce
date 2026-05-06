t=int(input())
while t:
    t-=1
    n=int(input())
    goals=list(map(int,input().split()))
    p =n=0
    for x in goals:
        if x>=0:
            p+=x
        else:
            n+=x
    if abs(n)>=p:
        print((abs(n)-p))
    else:
        print(-(p+n))
    