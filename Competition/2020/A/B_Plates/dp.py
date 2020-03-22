def dp(stacks, n, k, p) -> int:
    max_value = [[0] * (p+1) for _ in range(n)]

    # initial the table
    temp_sum = 0
    for i in range(1, p+1):
        if i <= k:
            temp_sum += stacks[0][i-1]
            max_value[0][i] = temp_sum
        else:
            max_value[0][i] = temp_sum

    # print(max_value)

    for j in range(1, n):
        curr_sums = [0]
        for idx in range(p):
            if idx < k:
                curr_sums.append(curr_sums[idx] + stacks[j][idx])
        # print(curr_sums)
        for total_pick in range(1, p + 1):
            for pick_curr_amount in range(min(total_pick, k) + 1):
                pick_last_amount = total_pick - pick_curr_amount
                # print(pick_last_amount, max_value[j-1][pick_last_amount])
                # print(pick_curr_amount, curr_sums[pick_curr_amount])
                # print('-')
                if pick_curr_amount <= k:
                    max_value[j][total_pick] = max(
                        max_value[j][total_pick], max_value[j-1][pick_last_amount] + curr_sums[pick_curr_amount])
                # else:
                #     max_value[j][total_pick] = max(
                #         max_value[j][total_pick], curr_sums[k] + max_value[j-1][pick_last_amount], max_value[j][total_pick-1])

        # print(max_value)

    return max_value[n-1][p]


# Input number of test cases
t = int(input())

for i in range(t):

    n, k, p = list(map(int, input().split()))

    stacks = []
    for j in range(n):
        stack = list(map(int, input().split()))
        stacks.append(stack)

    print('Case #{}:'.format(i+1), dp(stacks, n, k, p))
