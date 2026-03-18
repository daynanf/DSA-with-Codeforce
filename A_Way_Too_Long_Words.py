t=int(input())
while t:
    t-=1
    s=input()
    if len(s)>10:
        ans=f"{s[0]}{len(s)-2}{s[-1]}"
        print(ans)
    else :
        print(s)
    