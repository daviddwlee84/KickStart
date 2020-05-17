def update(A, x: int, v: int):
    A[x-1] = v

def query(A, l: int, r: int):
    """ sweetness score of the subarray """
    score = 0
    # print(A[l-1:r]) # subarray
    for i in range(l-1, r):
        # print(i, (-1)**(i - l-1), A[i], (i - (l-1) + 1), (-1)**(i - l-1) * A[i] * (i - (l-1) + 1))
        score += (-1)**(i - l-1) * A[i] * (i - (l-1) + 1)
    
    return score

def solve(n: int, q: int, A, operation):
    score = 0
    for op in operation:
        if op[0] == 'U':
            update(A, int(op[1]), int(op[2]))
        elif op[0] == 'Q':
            score += query(A, int(op[1]), int(op[2]))
    
    return int(score)


# Input number of test cases
t = int(input())

for i in range(t):

    n, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    operation = []
    for _ in range(q):
        input_temp = input().split()
        operation.append(input_temp)

    print('Case #{}:'.format(i + 1), solve(n, q, A, operation))

# TLE