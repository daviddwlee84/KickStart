def solve(n, H) -> int:
    peak = 0
    for i in range(1, n-1):
        if H[i-1] < H[i] and H[i] > H[i+1]:
            peak += 1

    return peak


# Input number of test cases
t = int(input())

for i in range(t):

    n = int(input())
    H = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, H))
