t= int(input())
while t:
    t-=1
    n=int(input())
    x=list(map(int,input().split()))
    if x[0]==1:
        print("YES")
    else:
        print("NO")