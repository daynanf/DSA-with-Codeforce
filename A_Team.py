x=int(input())
cnt=0
for _ in range(x):
    nums=input().split()
    y=nums.count("1")
    if y>1:
        cnt+=1
print(cnt)