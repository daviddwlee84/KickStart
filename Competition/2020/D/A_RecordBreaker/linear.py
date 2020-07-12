def solve(n, V) -> int:
    record_breaking_count = 0
    maximum_visitors = -1
    for i in range(n):
        if V[i] > maximum_visitors:
            maximum_visitors = V[i]
            if i == n - 1 or V[i] > V[i + 1]:
                record_breaking_count += 1

    return record_breaking_count


# Input number of test cases
t = int(input())

for i in range(t):

    n = int(input())
    V = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, V))
