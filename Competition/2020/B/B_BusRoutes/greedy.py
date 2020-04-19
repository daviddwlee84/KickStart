def solve(n, d, X) -> int:
    for i in reversed(range(n)):
        d = d - d % X[i]

    return d


# Input number of test cases
t = int(input())

for i in range(t):

    n, d = list(map(int, input().split()))
    X = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, d, X))
