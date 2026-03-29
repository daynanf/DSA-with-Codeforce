n= int(input())
x=list(map(int,input().split()))
x.sort()
pos=1
for i in range(n):
    if pos <= x[i]:
        pos+=1
    
print(pos-1)