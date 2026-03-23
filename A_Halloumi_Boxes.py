t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))

    #selection sort
    if k>1 or nums==sorted(nums) :
        print("YES")
    else:
        print("NO")

