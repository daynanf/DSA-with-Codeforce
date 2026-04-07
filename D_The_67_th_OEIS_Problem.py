import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    ans = []
    for i in range(1, n + 1):
        ans.append(i * (i + 1))

    print(*ans)