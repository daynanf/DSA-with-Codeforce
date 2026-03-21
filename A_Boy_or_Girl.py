s=input()
x={}
for n in s:
    x[n]=x.get(n,0)+1
if len(x)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")