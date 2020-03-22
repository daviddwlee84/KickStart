def sorting(arr, n, b) -> int:
    arr = sorted(arr)
    s = 0
    i = 0
    for a in arr:
        if a <= b:
            s += a
            b -= a
            i += 1
        else:
            break

    return i


# Input number of test cases
t = int(input())

for i in range(t):

    n, b = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), sorting(arr, n, b))
