t=int(input())
while t:
    t-=1
    x=int(input())
    cnt=0
    for i in range(x+1):
        if i%3 == i%5:
            cnt+=1
    print(cnt)