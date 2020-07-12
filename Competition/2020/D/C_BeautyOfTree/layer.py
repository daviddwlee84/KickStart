from functools import lru_cache


def solve(n: int, a: int, b: int, parents):
    layer = [1]
    for parent in parents:
        layer.append(layer[parent - 1] + 1)

    print(layer)
    return None


# Input number of test cases
t = int(input())

for i in range(t):

    n, a, b = list(map(int, input().split()))
    parents = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, a, b, parents))
