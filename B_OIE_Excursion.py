import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    forbidden = set()
    for i in range(1, n + 1):
        b = (a[i-1] + i) % m
        forbidden.add((m - b) % m)
        if len(forbidden) == m:
            print("NO")
            return
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()
