from itertools import permutations
from typing import List

# TLE at Test Set 2 (Larger one: 1 <= N <= 100)

# Permutation and try if it's possible


def solve(n: int, a: int, b: int, c: int):
    if a + b > 2 * n:
        return 'IMPOSSIBLE'
    if c > a or c > b:
        return 'IMPOSSIBLE'

    buildings = [(n - c + 1)] * c
    for i in reversed(range(1, n - c + 1)):
        buildings.append(i)

    for candidate in permutations(buildings, len(buildings)):
        if is_possible(n, a, b, c, candidate):
            return ' '.join(str(num) for num in candidate)

    return 'IMPOSSIBLE'


def is_possible(n: int, a: int, b: int, c: int, candidate: List[int]) -> bool:
    a_max = 0
    a_test = 0
    b_max = 0
    b_test = 0

    total_max = 0
    c_test = 0
    for i in range(len(candidate)):
        if candidate[i] > total_max:
            total_max = candidate[i]
            c_test = 1
        elif candidate[i] == total_max:
            c_test += 1

        if c_test > c:
            return False

        if candidate[i] >= a_max:
            a_max = candidate[i]
            a_test += 1

        if a_test > a:
            return False

        if candidate[-i - 1] >= b_max:
            b_max = candidate[-i - 1]
            b_test += 1

        if b_test > b:
            return False

    return (a == a_test) and (b == b_test) and (c == c_test)


# Input number of test cases
t = int(input())

for i in range(t):

    n, a, b, c = list(map(int, input().split()))

    print('Case #{}:'.format(i + 1), solve(n, a, b, c))
