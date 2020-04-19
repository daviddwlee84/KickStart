from collections import deque, defaultdict
# MLE on large case


def solve(w, h, l, u, r, d) -> float:
    grid = [[0] * w for _ in range(h)]
    grid[0][0] = 1
    come_from_left = [[False] * w for _ in range(h)]
    come_from_top = [[False] * w for _ in range(h)]
    come_from_left[0][0] = True
    come_from_top[0][0] = True

    # row: h, u, d, i
    # col: w, l, r, j

    # hole
    for i in range(h):  # row
        for j in range(w):  # col
            if (i + 1 >= u and j + 1 >= l) and (i + 1 <= d and j + 1 <= r):
                come_from_left[i][j] = True
                come_from_top[i][j] = True

    next_visit = deque([(0, 0)])
    while next_visit:
        i, j = next_visit.pop()
        next_visit.extendleft(
            mark(i, j, grid, come_from_left, come_from_top, w, h))

    return grid[h-1][w-1]


def mark(i, j, grid, come_from_left, come_from_top, w, h):
    next_visit = []

    if j == w - 1 and i != h - 1 and not come_from_left[i+1][j]:
        # rightmost column
        grid[i+1][j] += grid[i][j]
        next_visit.append((i+1, j))
        come_from_left[i+1][j] = True
    elif i == h - 1 and j != w - 1 and not come_from_top[i][j+1]:
        # bottommost row
        grid[i][j+1] += grid[i][j]
        next_visit.append((i, j+1))
        come_from_top[i][j+1] = True
    else:
        if i != h - 1 and not come_from_left[i+1][j]:
            grid[i+1][j] += grid[i][j] / 2
            next_visit.append((i+1, j))
            come_from_left[i+1][j] = True
        if j != w - 1 and not come_from_top[i][j+1]:
            grid[i][j+1] += grid[i][j] / 2
            next_visit.append((i, j+1))
            come_from_top[i][j+1] = True

    return next_visit


# Input number of test cases
t = int(input())

for i in range(t):

    w, h, l, u, r, d = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(w, h, l, u, r, d))
