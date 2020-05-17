def solve(n, k, A) -> int:
    count = 0
    temp_k = -1
    startCountdown = False
    for i in A:
        # print(i, temp_k, k, startCountdown)
        if i == k and not startCountdown:
            startCountdown = True
            temp_k = k - 1
        
        elif startCountdown:
            if temp_k > 1:
                if i != temp_k:
                    if i == k:
                        temp_k = k - 1
                    else:
                        # print('hoho')
                        startCountdown = False
                        temp_k = -1
                else:
                    temp_k -= 1
            elif i == temp_k == 1:
                count += 1
                # print('hihi')
                startCountdown = False
            # else:
            #     print('hehe')
            #     startCountdown = False

    return count


# Input number of test cases
t = int(input())

for i in range(t):

    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, k, A))
