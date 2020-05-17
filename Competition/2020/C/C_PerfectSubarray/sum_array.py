import functools

# to prevent determine same number
# https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
@functools.lru_cache(maxsize=None)
def isPerfectSquare(num: int) -> bool:
    if num >= 0:
        square = num ** 0.5
        return int(square) == square
    else:
        return False

def solve(n: int, A):
    count = 0
    sum_array = [0]
    for num in A:
        sum_array.append(sum_array[-1] + num)

    for window_size in range(1, n + 1):
        for start in range(len(A) - window_size + 1):
            end = start + window_size
            if isPerfectSquare(sum_array[end] - sum_array[start]):
                count += 1
    
    return count


# Input number of test cases
t = int(input())

for i in range(t):

    n = int(input())
    A = list(map(int, input().split()))

    print('Case #{}:'.format(i + 1), solve(n, A))

# Only pass small testcases
