t=int(input())
while t:
    t-=1
    nX,nS=list(map(int,input().split()))
    x=input()
    s=input()
    cnt=0
    if s in x:
            print(0) 
            continue
    for _ in range(5):
        x+=x
        cnt+=1
        if s in x:
            print(cnt)
            break
    if s  not in x:
            print(-1) 
   
    