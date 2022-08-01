n = int(input())
plan = list(input().split())
x, y = 1, 1

dx = [ 0, 0, -1, 1 ]
dy = [ -1, 1, 0, 0 ]
move_types = [ 'L', 'R', 'U', 'D' ]

for p in plan:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    else:
        x = nx
        y = ny

print(x, y)