"""

1 5 100 500 1

ABCD(ABC)

2 3 4 5 6 7 8 9
ABCD[A]BCD

2 3 4 5 4 7 8 9
ABCDABCD
"""


def solve(k, A) -> int:
    continueous_add = 1
    continueous_minus = 1
    previous = A[0]
    rule_break_count = 0
    for curr in A[1:]:
        if previous < curr:
            continueous_add += 1
            continueous_minus = 1
        elif previous > curr:
            continueous_minus += 1
            continueous_add = 1

        if continueous_add == 5 or continueous_minus == 5:
            rule_break_count += 1
            continueous_add = 1
            continueous_minus = 1

        previous = curr

    return rule_break_count


# Input number of test cases
t = int(input())

for i in range(t):

    k = int(input())
    A = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(k, A))
