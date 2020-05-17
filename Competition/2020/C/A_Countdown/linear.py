def solve(n, k, A) -> int:
    count = 0
    temp_k = -1
    for num in A:
        if num == k:
            # start counting
            temp_k = k
        
        if num != temp_k:
            # just go to next number
            temp_k = -1
            continue
    
        if num == temp_k == 1:
            # reach the end
            count += 1
        
        temp_k -= 1
            

    return count


# Input number of test cases
t = int(input())

for i in range(t):

    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, k, A))
