def solve(n, p):
    p = [x - 1 for x in p]  
    memo = {}
    
    def dfs(pos, marked_tuple):
        if pos >= n or pos in marked_tuple:
            return 0
        
        if (pos, marked_tuple) in memo:
            return memo[(pos, marked_tuple)]
        skip = dfs(pos + 1, marked_tuple)
        
        new_marked = tuple(sorted(set(marked_tuple) | {p[pos]}))
        sit = 1 + dfs(pos + 1, new_marked)
        
        result = max(skip, sit)
        memo[(pos, marked_tuple)] = result
        return result
    
    return dfs(0, ())

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
