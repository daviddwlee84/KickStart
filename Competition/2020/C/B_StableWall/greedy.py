from collections import defaultdict
def solve(r, c, grid):
    """ Put down in reverse pick up order """

    blocked_by = defaultdict(set)

    previous_row = []
    for row_items in grid:
        if not previous_row:
            for item in row_items:
                blocked_by[item] = set()
        else:
            for prev_item, item in zip(previous_row, row_items):
                if prev_item != item:
                    blocked_by[item].add(prev_item)
        previous_row = row_items
    
    to_pickup = list(blocked_by.keys())
    pickup_order = []

    while to_pickup:
        found = False
        for candidate in to_pickup.copy():
            if not found and not blocked_by[candidate]:
                # doesn't block by others
                to_pickup.remove(candidate)
                pickup_order.append(candidate)
                for others in blocked_by.keys():
                    if others != candidate:
                        blocked_by[others] -= set([candidate])
                found = True
        
        if not found:
            break
    
    if not to_pickup:
        return ''.join(reversed(pickup_order))
    else:
        return -1


# Input number of test cases
t = int(input())

for i in range(t):

    r, c = list(map(int, input().split()))
    grid = []
    for row in range(r):
        grid.append(list(input()))
    
    print('Case #{}:'.format(i+1), solve(r, c, grid))
