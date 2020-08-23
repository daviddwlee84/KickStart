def solve(n, A) -> int:
    if len(A) <= 2:
        return len(A)

    diff = [A[i + 1] - A[i] for i in range(len(A) - 1)]

    longest_same = 1
    curr_same = 1
    prev = None
    for d in diff:
        if d == prev:
            curr_same += 1
            longest_same = max(longest_same, curr_same)
        else:
            curr_same = 1
        prev = d

    return longest_same + 1


# Input number of test cases
t = int(input())

for i in range(t):

    n = int(input())
    A = list(map(int, input().split()))

    print('Case #{}:'.format(i + 1), solve(n, A))
