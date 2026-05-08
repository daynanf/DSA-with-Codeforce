t=int(input())
while t:
    t-=1
    x,k=list(map(int,input().split()))
    s=input()
    freq=dict()
    numOdds=numEvens=0
    for x in s:
        freq[x]=freq.get(x,0)+1
    freqs=list(freq.values())
    for x in freqs:
        if x%2:
            numOdds+=1
        else:
            numEvens+=1
    if numOdds-1>k:
        print("NO")
    else:
        print("YES")