t= int(input())
while t:
    t-=1
    n,x=list(map(int,input().split()))
    gas=list(map(int,input().split()))
    fuels=[]
    for i,g in enumerate(gas):
        if i==0:
            fuels.append(g)
            if len(gas)==1:
                fuels.append(2*(x-g))
            else:
                fuels.append(gas[i+1]-g)
        elif i+1==n:
            fuels.append(2*(x-g))
        else:
            fuels.append(gas[i+1]-g)
    ans=max(fuels)
    print(ans)