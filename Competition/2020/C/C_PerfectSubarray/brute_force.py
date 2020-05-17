def isPerfectSquare(num: int) -> bool:
    if num >= 0:
        square = num ** 0.5
        return int(square) == square
    else:
        return False

def solve(n: int, A):
    count = 0
    for window_size in range(1, n + 1):
        for start in range(len(A) - window_size + 1):
            if isPerfectSquare(sum(A[start:start + window_size])):
                count += 1
    
    return count


# Input number of test cases
t = int(input())

for i in range(t):

    n = int(input())
    A = list(map(int, input().split()))

    print('Case #{}:'.format(i + 1), solve(n, A))

# TLE