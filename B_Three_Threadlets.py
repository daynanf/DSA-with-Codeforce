t=int(input())
while t:
    t-=1
    nums=list(map(int,input().split()))
    a=min(nums)
    c=max(nums)
    s=sum(nums)
    b=s-a-c
    if a == c :
        print("YES")
        continue
    if not (b%a==c%a==0):
        print("NO")
        continue
    ans=(c-a)/a + (b-a)/a
    if ans>3:
        print("NO")
        continue
    elif ans <=3 :        
        print("YES")
        continue
