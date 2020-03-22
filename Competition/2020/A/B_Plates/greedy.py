# Deprecated (Wrong Answer)


def greedy(stacks, n, k, p) -> int:
    ratios = []
    for stack in stacks:
        temp_ratio = []
        # temp_sum = 0
        for i, beauty_value in enumerate(stack):
            # temp_sum += beauty_value
            # temp_ratio.append(temp_sum / (i + 1))
            temp_ratio.append(beauty_value / (i + 1))
        ratios.append(temp_ratio)

    print(ratios)

    answer = 0
    pick_from = [0] * n
    for i in range(p):
        temp_max_stack = 0
        temp_max = 0
        for j in range(n):
            if pick_from[j] < k and ratios[j][pick_from[j]] > temp_max:
                temp_max = ratios[j][pick_from[j]]
                temp_max_stack = j

        answer += stacks[temp_max_stack][pick_from[temp_max_stack]]
        pick_from[temp_max_stack] += 1

    print(pick_from)

    return answer


# Input number of test cases
t = int(input())

for i in range(t):

    n, k, p = list(map(int, input().split()))

    stacks = []
    for j in range(n):
        stack = list(map(int, input().split()))
        stacks.append(stack)

    print('Case #{}:'.format(i+1), greedy(stacks, n, k, p))
